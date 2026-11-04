"""Gera árvores a partir dos index.md dos materiais e referências entre trilhas."""
from __future__ import annotations

import json
import re
import tomllib
from collections import defaultdict
from html import escape
from pathlib import Path
from urllib.parse import quote, urlsplit

import yaml

ROOT = Path("docs/trilhas/tutoriais")
MARCADOR = "<!-- GERAR_CARDS -->"
with Path("zensical.toml").open("rb") as arquivo:
    PREFIXO = urlsplit(tomllib.load(arquivo)["project"]["site_url"]).path.rstrip("/")


def metadados(arquivo: Path) -> dict:
    texto = arquivo.read_text(encoding="utf-8-sig").lstrip()
    trecho = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", texto, re.S)
    if not trecho:
        raise ValueError(f"{arquivo}: metadados YAML ausentes")
    try:
        dados = yaml.safe_load(trecho.group(1))
    except yaml.YAMLError as erro:
        raise ValueError(f"{arquivo}: YAML inválido: {erro}") from erro
    if not isinstance(dados, dict):
        raise ValueError(f"{arquivo}: metadados devem ser um mapa")
    return dados


def texto(dados: dict, chave: str, arquivo: Path) -> str:
    valor = dados.get(chave)
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{arquivo}: {chave} deve ser texto não vazio")
    return valor.replace(r"\#", "#").strip()


def descobrir() -> tuple[dict, dict, dict]:
    trilhas, todos, reais = {}, {}, {}
    nomes_trilhas = set()
    for indice in sorted(ROOT.glob("*/index.md"), key=lambda p: p.parent.name.casefold()):
        trilha = indice.parent.name
        if trilha.casefold() in nomes_trilhas:
            raise ValueError(f"{indice}: trilha duplicada ignorando maiúsculas")
        nomes_trilhas.add(trilha.casefold())
        pagina = indice.parent / "conteudo.md"
        if not pagina.is_file():
            continue
        fonte = pagina.read_text(encoding="utf-8")
        indices = sorted((indice.parent / "materiais").glob("*/index.md"), key=lambda p: p.parent.name.casefold())
        if not indices and MARCADOR not in fonte:
            continue
        if fonte.count(MARCADOR) != 1:
            raise ValueError(f"{pagina}: esperado exatamente um marcador {MARCADOR}")
        cards, nomes = {}, set()
        for arquivo in indices:
            nome = arquivo.parent.name
            if nome.casefold() in nomes:
                raise ValueError(f"{arquivo}: card duplicado ignorando maiúsculas")
            nomes.add(nome.casefold())
            dados = metadados(arquivo)
            pai, nivel, ordem = dados.get("pai"), dados.get("nivel"), dados.get("ordem")
            if pai is not None and (not isinstance(pai, str) or not pai.strip()):
                raise ValueError(f"{arquivo}: pai deve ser null ou nome de pasta")
            if type(nivel) is not int or nivel < 0:
                raise ValueError(f"{arquivo}: nivel deve ser inteiro >= 0")
            if type(ordem) is not int or ordem < 0:
                raise ValueError(f"{arquivo}: ordem deve ser inteiro >= 0")
            referencia = dados.get("referencia")
            if referencia is not None:
                if not isinstance(referencia, str) or not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9-]+", referencia):
                    raise ValueError(f"{arquivo}: referencia deve ser 'trilha/pasta-do-tutorial'")
                if "destino" in dados:
                    raise ValueError(f"{arquivo}: referência não deve definir destino")
            else:
                titulo = texto(dados, "title", arquivo)
                descricao = dados.get("description")
                if not isinstance(descricao, str):
                    raise ValueError(f"{arquivo}: description deve ser texto")
                destino = texto(dados, "destino", arquivo)
                if not re.fullmatch(r"[A-Za-z0-9_-][A-Za-z0-9._-]*\.md", destino):
                    raise ValueError(f"{arquivo}: destino deve ser Markdown da mesma pasta")
                alvo = arquivo.parent / destino
                if not alvo.is_file():
                    raise ValueError(f"{arquivo}: destino inexistente: {alvo}")
                reais[f"{trilha}/{nome}"] = {
                    "titulo": titulo, "descricao": descricao.replace(r"\#", "#"),
                    "url": f"{PREFIXO}/trilhas/tutoriais/{quote(trilha, safe='')}/materiais/{quote(nome, safe='')}/{quote(alvo.stem, safe='')}/",
                }
            card = {"id": f"{trilha}/{nome}", "arquivo": arquivo, "pai": pai,
                    "nivel": nivel, "ordem": ordem, "referencia": referencia}
            cards[nome] = card
            todos[card["id"]] = card
        trilhas[trilha] = (pagina, cards)
    return trilhas, todos, reais


def resolver(todos: dict, reais: dict) -> dict:
    saida = dict(reais)
    nomes = defaultdict(list)
    for identificador in todos:
        nomes[identificador.casefold()].append(identificador)

    def seguir(identificador: str, caminho: list[str]) -> dict:
        if identificador in saida:
            return saida[identificador]
        card = todos[identificador]
        if identificador in caminho:
            raise ValueError(f"{card['arquivo']}: referência circular: {' -> '.join(caminho + [identificador])}")
        alvo = card["referencia"]
        candidatos = nomes.get(alvo.casefold(), [])
        if not candidatos:
            raise ValueError(f"{card['arquivo']}: referência inexistente: {alvo}")
        if len(candidatos) > 1:
            raise ValueError(f"{card['arquivo']}: referência ambígua: {alvo}")
        if candidatos[0] != alvo:
            raise ValueError(f"{card['arquivo']}: referência com maiúsculas diferentes: {alvo}; use {candidatos[0]}")
        saida[identificador] = seguir(alvo, caminho + [identificador])
        return saida[identificador]

    for identificador, card in todos.items():
        if card["referencia"]:
            seguir(identificador, [])
    return saida


def hierarquia(trilha: str, cards: dict) -> tuple[dict, dict]:
    raizes = [nome for nome, card in cards.items() if card["pai"] is None]
    if len(raizes) != 1:
        raise ValueError(f"{ROOT / trilha / 'materiais'}: esperado um único card raiz; encontrados {len(raizes)}")
    filhos = defaultdict(list)
    for nome, card in cards.items():
        pai = card["pai"]
        if pai is None:
            if card["nivel"] != 0:
                raise ValueError(f"{card['arquivo']}: raiz deve ter nivel 0")
        elif pai not in cards:
            raise ValueError(f"{card['arquivo']}: pai inexistente na mesma árvore: {pai}")
        else:
            filhos[pai].append(nome)
    visitados = set()

    def visitar(nome: str, caminho: set[str]) -> None:
        card = cards[nome]
        if nome in caminho:
            raise ValueError(f"{card['arquivo']}: ciclo na hierarquia")
        if nome in visitados:
            return
        caminho = caminho | {nome}
        for filho in filhos[nome]:
            esperado = card["nivel"] + 1
            if cards[filho]["nivel"] != esperado:
                raise ValueError(f"{cards[filho]['arquivo']}: nivel deve ser {esperado} conforme pai {nome}")
            visitar(filho, caminho)
        visitados.add(nome)

    visitar(raizes[0], set())
    if len(visitados) != len(cards):
        pendentes = [str(cards[n]["arquivo"]) for n in cards if n not in visitados]
        raise ValueError(f"{ROOT / trilha / 'materiais'}: cards desconectados ou em ciclo: {', '.join(pendentes)}")
    for grupo in filhos.values():
        grupo.sort(key=lambda nome: (cards[nome]["ordem"], nome))
    return cards[raizes[0]], filhos


def renderizar(trilha: str, cards: dict, dados: dict) -> str:
    if not cards:
        return "<p>Esta trilha ainda não possui tutoriais.</p>"
    raiz, filhos = hierarquia(trilha, cards)

    def no(card: dict, eh_raiz: bool = False) -> str:
        nome = card["arquivo"].parent.name
        info = dados[card["id"]]
        descendentes = filhos[nome]
        classe = ' class="arvore-raiz arvore-com-filhos"' if eh_raiz and descendentes else (' class="arvore-raiz"' if eh_raiz else "")
        descricao = f'<span>{escape(info["descricao"])}</span>' if info["descricao"] else ""
        partes = [f'<li{classe} data-id="{escape(card["id"], quote=True)}">',
                  f'<a class="arvore-card" href="{escape(info["url"], quote=True)}"><strong>{escape(info["titulo"])}</strong>{descricao}</a>']
        if descendentes:
            partes.append('<ul class="arvore-filhos">')
            partes.extend(no(cards[filho]) for filho in descendentes)
            partes.append("</ul>")
        partes.append("</li>")
        return "\n".join(partes)

    return '<nav class="arvore-hierarquia" aria-label="Árvore dos materiais">\n<ul class="arvore-topo">\n' + no(raiz, True) + '\n</ul>\n</nav>'


def redirecionamento(url: str) -> str:
    return ('# Tutorial transferido\n\n'
            f'Este material foi movido para [seu novo endereço]({url}).\n\n'
            f'<meta http-equiv="refresh" content="0; url={escape(url, quote=True)}">\n'
            f'<script>window.location.replace({json.dumps(url)});</script>\n')


def preparar_redirecionamentos(reais: dict) -> dict:
    saida = {}
    mapa = Path("scripts/redirecionamentos_antigos.json")
    if mapa.is_file():
        entradas = json.loads(mapa.read_text(encoding="utf-8"))
        for antigo, novo in entradas.items():
            if not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9-]+", antigo):
                raise ValueError(f"{mapa}: identificador antigo inválido: {antigo}")
            # Unity e VR mantêm os nomes de pasta originais; o valor do mapa
            # também registra o endereço intermediário em docs/materiais/.
            destino = novo if novo in reais else antigo if antigo in reais else None
            if destino is None:
                raise ValueError(f"{mapa}: destino inexistente: {novo}")
            area, slug = novo.split("/")
            saida[Path("docs/materiais") / area / f"{slug}.md"] = redirecionamento(reais[destino]["url"])
            trilha, pasta = antigo.split("/")
            caminho = ROOT / trilha / "materiais" / pasta / "conteudo.md"
            if destino == antigo:
                continue  # O endereço antigo ainda é o conteúdo real.
            if caminho.is_file():
                raise ValueError(f"{mapa}: redirecionamento sobrescreveria tutorial: {caminho}")
            saida[caminho] = redirecionamento(reais[destino]["url"])
    return saida


def main() -> None:
    trilhas, todos, reais = descobrir()
    dados = resolver(todos, reais)
    estilo = f"<style>\n{Path('scripts/arvore.css').read_text(encoding='utf-8')}\n</style>"
    paginas = {}
    for nome, (pagina, cards) in trilhas.items():
        arvore = renderizar(nome, cards, dados)
        paginas[pagina] = pagina.read_text(encoding="utf-8").replace(MARCADOR, arvore + "\n" + estilo, 1)
        print(f"{nome}: {len(cards)} cards")
    redirecionamentos = preparar_redirecionamentos(reais)
    # Só escreve após validar todas as árvores e todos os alvos.
    for caminho, conteudo in paginas.items():
        caminho.write_text(conteudo, encoding="utf-8")
    for caminho, conteudo in redirecionamentos.items():
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(conteudo, encoding="utf-8")
    print(f"Total: {len(reais)} tutoriais, {len(dados)} cards, {len(redirecionamentos)} redirecionamentos")


if __name__ == "__main__":
    main()
