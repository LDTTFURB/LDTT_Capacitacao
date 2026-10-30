from pathlib import Path
from collections import defaultdict
from html import escape
from urllib.parse import quote, urlsplit
import os
import re
import sys
import yaml

ROOT = Path("docs/trilhas/tutoriais")
MARCADOR = "<!-- GERAR_CARDS -->"
SITE = "/LDTT_Capacitacao/trilhas/tutoriais"


def encerrar_se_houver(erros):
    # Um erro impede a publicacao: o site anterior continua no ar.
    for erro in erros:
        print(f"ERRO: {erro}")

    if erros:
        sys.exit(1)


def ler_metadados(arquivo):
    texto = arquivo.read_text(encoding="utf-8-sig")
    texto = texto.lstrip(" \t\r\n")

    resultado = re.match(
        r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)",
        texto,
        re.DOTALL
    )

    if not resultado:
        raise ValueError(f"Metadados ausentes: {arquivo}")

    dados = yaml.safe_load(resultado.group(1))

    if not isinstance(dados, dict):
        raise ValueError(f"Metadados invalidos: {arquivo}")

    return dados


def validar_trilha(dados):
    titulo = dados.get("title")
    descricao = dados.get("description")
    tags = dados.get("tags")
    relacionadas = dados.get("relacionadas", [])

    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("title invalido")

    if not isinstance(descricao, str):
        raise ValueError("description invalida")

    if (
        not isinstance(tags, list)
        or not tags
        or not all(isinstance(t, str) and t.strip() for t in tags)
    ):
        raise ValueError("tags invalidas")

    if not isinstance(relacionadas, list):
        raise ValueError("relacionadas deve ser uma lista")


def ler_trilhas():
    """Valida o index.md de cada trilha e devolve {pasta: metadados}."""
    trilhas = {}
    erros = []

    for arquivo in sorted(ROOT.glob("*/index.md"), key=lambda p: p.parent.name.lower()):
        try:
            dados = ler_metadados(arquivo)
            validar_trilha(dados)
            trilhas[arquivo.parent.name] = dados
        except (ValueError, yaml.YAMLError) as erro:
            erros.append(f"{arquivo}: {erro}")

    for pasta, dados in trilhas.items():
        pai = dados.get("pai")

        # Um unico nivel de subtrilhas tambem impede ciclos entre trilhas.
        if pai is not None and (
            pai not in trilhas or trilhas[pai].get("pai") is not None
        ):
            erros.append(f"{pasta}: pai deve ser uma trilha de primeiro nivel: {pai}")

        for relacionada in dados.get("relacionadas", []):
            if relacionada not in trilhas:
                erros.append(f"{pasta}: trilha relacionada inexistente: {relacionada}")

    encerrar_se_houver(erros)

    return trilhas


def gerar_card_trilha(pasta, dados, subtrilha=False):
    # Novo formato: abre conteudo.md.
    # Compatibilidade com trilhas antigas: abre index.md.
    link = f"{SITE}/{quote(pasta, safe='')}/"

    if (ROOT / pasta / "conteudo.md").exists():
        link += "conteudo/"

    nomes_tags = ", ".join(dados["tags"])
    atributos = " data-subtrilha hidden" if subtrilha else ""

    return f"""
<a class="ldtt-card"
   href="{escape(link, quote=True)}"
   data-tags="{escape(nomes_tags, quote=True)}"{atributos}>
  <strong>{escape(dados["title"])}</strong>
  <span>{escape(dados["description"])}</span>
  <small>{escape(nomes_tags)}</small>
</a>
"""


def montar_grade(pastas, trilhas):
    cards = "\n".join(gerar_card_trilha(pasta, trilhas[pasta]) for pasta in pastas)
    return f'<div class="ldtt-grid">\n{cards}\n</div>'


def gerar_link(arquivo, destino):
    url = urlsplit(destino)

    # Links externos
    if url.scheme in ("http", "https") and url.netloc:
        return destino, True

    if url.scheme or url.netloc:
        raise ValueError("URL externa invalida")

    caminho = Path(destino)

    if (
        caminho.is_absolute()
        or ".." in caminho.parts
        or caminho.suffix.lower() != ".md"
        or url.query
        or url.fragment
    ):
        raise ValueError("Destino Markdown invalido")

    arquivo_destino = arquivo.parent / caminho

    if not arquivo_destino.is_file():
        raise ValueError(f"Destino inexistente: {destino}")

    trilha = quote(arquivo.parent.parent.parent.name, safe="")
    tutorial = quote(arquivo.parent.name, safe="")

    partes = list(caminho.parts)

    if partes[-1] == "index.md":
        partes.pop()
    else:
        partes[-1] = Path(partes[-1]).stem

    caminho_site = "/".join(
        quote(parte, safe="") for parte in partes
    )

    link = f"{SITE}/{trilha}/materiais/{tutorial}/"

    if caminho_site:
        link += f"{caminho_site}/"

    return link, False



def gerar_card(arquivo, dados):
    titulo = dados.get("title")
    descricao = dados.get("description")
    destino = dados.get("destino", "conteudo.md")

    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("title invalido")

    if not isinstance(descricao, str):
        raise ValueError("description invalida")

    if not isinstance(destino, str) or not destino.strip():
        raise ValueError("destino invalido")

    # Os cards usam HTML, portanto o escape Markdown nao aparece no texto.
    titulo = titulo.replace(r"\#", "#")
    descricao = descricao.replace(r"\#", "#")

    link, externo = gerar_link(arquivo, destino.strip())

    atributos = ""

    if externo:
        atributos = ' target="_blank" rel="noopener noreferrer"'

    card = f"""
<a class="arvore-card"
   href="{escape(link, quote=True)}"{atributos}>
  <strong>{escape(titulo)}</strong>
  <span>{escape(descricao)}</span>
</a>
"""

    ordem = dados.get("ordem", 0)

    if type(ordem) is not int or ordem < 0:
       raise ValueError("ordem deve ser um inteiro >= 0")

    return dict(
        titulo=dados["title"],
        pai=dados.get("pai"),
        ordem=ordem,
        destino=destino.strip(),
        externo=externo,
        card=card,
    )


CSS_HIERARQUIA = """
<style>
.arvore-hierarquia {
  --linha: var(--md-default-fg-color--lightest);
  --conector: var(--md-default-fg-color--lighter, #d9dde3);
  --espaco-ramos: 20px;
  margin: 24px 0;
}
/* Reinicia tambem os espacamentos de listas aplicados pelo tema. */
.md-typeset nav.arvore-hierarquia ul,
.md-typeset nav.arvore-hierarquia ul > li {
  list-style: none; margin: 0; padding: 0; min-width: 0; box-sizing: border-box;
}
.md-typeset nav.arvore-hierarquia ul > li { position: relative; }
.arvore-hierarquia .arvore-card {
  display: flex; flex-direction: column; gap: 8px; padding: 14px;
  border: 1px solid var(--linha); border-radius: 10px; color: inherit;
  text-decoration: none; overflow-wrap: break-word;
}
.arvore-hierarquia .arvore-card:hover,
.arvore-hierarquia .arvore-card:focus-visible { border-color: var(--md-primary-fg-color); }
.arvore-hierarquia .arvore-card strong { font-size: 14px; }
.arvore-hierarquia .arvore-card span { font-size: 12px; opacity: .75; }
.arvore-hierarquia .arvore-raiz > .arvore-card {
  position: relative; max-width: 360px; margin: 0 auto;
}
.arvore-hierarquia .arvore-raiz > .arvore-card:not(:last-child)::after {
  content: ''; position: absolute; left: 50%; top: 100%; height: 20px;
  border-left: 2px solid var(--conector);
}
/* Cada filho desenha o seu segmento vertical e o cotovelo ate o card.
   O ultimo segmento termina na ligacao, sem prolongar a linha para baixo. */
.md-typeset nav.arvore-hierarquia ul.arvore-filhos {
  margin-left: 8px; padding-left: 12px;
}
.md-typeset nav.arvore-hierarquia ul.arvore-filhos > li { padding-top: 16px; }
.arvore-hierarquia ul.arvore-filhos > li::before {
  content: ''; position: absolute; top: 0; bottom: 0; left: -12px;
  border-left: 2px solid var(--conector);
}
.arvore-hierarquia ul.arvore-filhos > li:last-child::before { bottom: auto; height: 38px; }
.arvore-hierarquia ul.arvore-filhos > li::after {
  content: ''; position: absolute; left: -12px; top: 38px; width: 12px;
  border-top: 2px solid var(--conector);
}
/* A linha horizontal cobre o intervalo inteiro entre os ramos da raiz. */
.md-typeset nav.arvore-hierarquia .arvore-raiz > ul.arvore-filhos {
  display: flex; align-items: flex-start; gap: var(--espaco-ramos);
  margin: 0; padding: 40px 0 0;
}
.md-typeset nav.arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li {
  flex: 1 1 0; padding: 0;
}
.arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li::before {
  top: -20px; bottom: auto; left: calc(var(--espaco-ramos) / -2);
  right: calc(var(--espaco-ramos) / -2); height: 0;
  border: 0; border-top: 2px solid var(--conector);
}
.arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li:first-child::before { left: 50%; }
.arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li:last-child::before { right: 50%; height: 0; }
.arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li::after {
  left: 50%; top: -20px; width: 0; height: 20px;
  border: 0; border-left: 2px solid var(--conector);
}
/* Um filho unico fica alinhado a raiz, em vez de ocupar toda a largura. */
@media (min-width: 901px) {
  .md-typeset nav.arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li:only-child {
    flex: 0 1 360px; margin: 0 auto;
  }
  .arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li:only-child::after {
    top: -21px; height: 21px;
  }
}
@media (max-width: 900px) {
  .arvore-hierarquia .arvore-raiz > .arvore-card { margin: 0; max-width: none; }
  .arvore-hierarquia .arvore-raiz > .arvore-card:not(:last-child)::after { display: none; }
  .md-typeset nav.arvore-hierarquia .arvore-raiz > ul.arvore-filhos {
    display: block; margin-left: 12px; padding: 0 0 0 20px;
  }
  .md-typeset nav.arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li { padding-top: 16px; }
  .arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li::before,
  .arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li:first-child::before,
  .arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li:last-child::before {
    top: 0; bottom: 0; left: -20px; right: auto; height: auto;
    border: 0; border-left: 2px solid var(--conector);
  }
  .arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li:last-child::before { bottom: auto; height: 38px; }
  .arvore-hierarquia .arvore-raiz > ul.arvore-filhos > li::after {
    left: -20px; top: 38px; width: 20px; height: 0;
    border: 0; border-top: 2px solid var(--conector);
  }
}
</style>
"""


def agrupar_filhos(nos):
    """Valida os pais e devolve os filhos de cada no, ja ordenados."""
    filhos = defaultdict(list)

    for identificador, no in nos.items():
        pai = no["pai"]
        if pai is not None and (not isinstance(pai, str) or pai not in nos):
            raise ValueError(f"Pai inexistente ou invalido: {identificador}")
        filhos[pai].append(identificador)

    for lista in filhos.values():
        lista.sort(key=lambda item: (nos[item]["ordem"], item))

    return filhos


def montar_hierarquia(nos):
    """Valida a arvore antes de gerar uma lista aninhada de materiais."""
    filhos = agrupar_filhos(nos)

    # Percorre os pais de todos os nos, inclusive componentes sem uma raiz.
    profundidades = {}
    visitando = set()

    def profundidade(identificador):
        if identificador in visitando:
            raise ValueError(f"Ciclo na arvore: {identificador}")
        if identificador not in profundidades:
            visitando.add(identificador)
            pai = nos[identificador]["pai"]
            profundidades[identificador] = 0 if pai is None else profundidade(pai) + 1
            visitando.remove(identificador)
        return profundidades[identificador]

    for identificador in nos:
        profundidade(identificador)
    if len(filhos[None]) != 1:
        raise ValueError(f"A arvore deve ter uma unica raiz sem pai: {filhos[None]}")

    def renderizar(pai):
        partes = ['<ul class="arvore-filhos">' if pai is not None else '<ul class="arvore-topo">']
        for identificador in filhos[pai]:
            no = nos[identificador]
            classe = ' class="arvore-raiz"' if pai is None else ''
            partes.append(f'<li{classe} data-id="{escape(identificador, quote=True)}" data-nivel="{profundidades[identificador]}">')
            partes.append(no["card"])
            if filhos[identificador]:
                partes.append(renderizar(identificador))
            partes.append('</li>')
        partes.append('</ul>')
        return '\n'.join(partes)

    return '<nav class="arvore-hierarquia" aria-label="Árvore dos materiais">\n' + renderizar(None) + '\n</nav>\n' + CSS_HIERARQUIA


def gerar_navegacao(materiais, nos):
    """Acrescenta a cada material os links para o pai e os filhos na arvore."""
    filhos = agrupar_filhos(nos)

    for identificador, no in nos.items():
        if no["externo"]:
            continue

        arquivo = materiais / identificador / no["destino"]

        def link(outro):
            if nos[outro]["externo"]:
                return nos[outro]["destino"]
            alvo = materiais / outro / nos[outro]["destino"]
            return Path(os.path.relpath(alvo, arquivo.parent)).as_posix()

        partes = []

        if no["pai"] is not None:
            partes.append(f'[← Anterior: {nos[no["pai"]]["titulo"]}]({link(no["pai"])})')

        proximos = filhos[identificador]

        if len(proximos) == 1:
            partes.append(f'[Próximo: {nos[proximos[0]]["titulo"]} →]({link(proximos[0])})')
        elif proximos:
            lista = "\n".join(f'- [{nos[p]["titulo"]} →]({link(p)})' for p in proximos)
            partes.append(f"**Próximos:**\n\n{lista}")

        if partes:
            with arquivo.open("a", encoding="utf-8") as saida:
                saida.write("\n\n## Navegação\n\n" + "\n\n".join(partes) + "\n")


def ler_materiais(pasta_materiais, erros):
    nos = {}

    for arquivo in sorted(pasta_materiais.glob("*/index.md"), key=lambda p: p.parent.name.lower()):
        try:
            nos[arquivo.parent.name] = gerar_card(arquivo, ler_metadados(arquivo))
        except (ValueError, yaml.YAMLError) as erro:
            erros.append(f"{arquivo}: {erro}")

    return nos


def processar_trilha(pasta, trilhas, erros):
    trilha = ROOT / pasta
    arquivo_conteudo = trilha / "conteudo.md"
    pasta_materiais = trilha / "materiais"

    nos = ler_materiais(pasta_materiais, erros)
    subtrilhas = [p for p, dados in trilhas.items() if dados.get("pai") == pasta]
    relacionadas = trilhas[pasta].get("relacionadas", [])

    if not arquivo_conteudo.is_file():
        # Trilhas sem materiais podem ter so o index.md.
        if nos or subtrilhas or relacionadas:
            raise ValueError("conteudo.md ausente")
        return

    # Altera o arquivo apenas no ambiente temporário do build.
    texto = arquivo_conteudo.read_text(encoding="utf-8-sig")

    blocos = []

    if subtrilhas:
        blocos.append(montar_grade(subtrilhas, trilhas))

    if nos:
        blocos.append(montar_hierarquia(nos))
        gerar_navegacao(pasta_materiais, nos)

    arvore = "\n\n".join(blocos)

    # Sem o marcador, os cards entram no fim da página.
    if MARCADOR in texto:
        texto = texto.replace(MARCADOR, arvore or "<p>Nenhum tutorial cadastrado ainda.</p>", 1)
    elif arvore:
        texto += f"\n\n## Conteúdos\n\n{arvore}\n"

    if relacionadas:
        texto += f"\n\n## Trilhas relacionadas\n\n{montar_grade(relacionadas, trilhas)}\n"

    arquivo_conteudo.write_text(texto, encoding="utf-8")

    print(f"{pasta}: {len(nos)} materiais e {len(subtrilhas)} subtrilhas")


if __name__ == "__main__":
    trilhas = ler_trilhas()
    erros = []

    for pasta in trilhas:
        try:
            processar_trilha(pasta, trilhas, erros)
        except ValueError as erro:
            erros.append(f"{pasta}: {erro}")

    encerrar_se_houver(erros)
