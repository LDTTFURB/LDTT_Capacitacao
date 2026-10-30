"""Gera as árvores de trilhas a partir dos roteiros e dos arquivos .md.

Bolsistas escrevem somente docs/materiais/<area>/<tutorial>.md.
Organizadores editam somente roteiros/<trilha>.md, com listas indentadas.
O script é executado no GitHub Actions; não commitamos árvores geradas.
"""

from __future__ import annotations

import json
import re
import tomllib
from html import escape
from pathlib import Path
from urllib.parse import quote, urlsplit

DOCS = Path("docs")
MATERIAIS = DOCS / "materiais"
TRILHAS = DOCS / "trilhas" / "tutoriais"
ROTEIROS = Path("roteiros")
MARCADOR = "<!-- GERAR_CARDS -->"

with Path("zensical.toml").open("rb") as configuracao:
    SITE_URL = tomllib.load(configuracao)["project"]["site_url"]
PREFIXO = urlsplit(SITE_URL).path.rstrip("/")

# O estilo original da árvore foi preservado, inclusive a correção dos ramos internos.
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
.arvore-hierarquia .arvore-raiz > .arvore-card::after {
  content: ''; position: absolute; left: 50%; top: 100%; height: 20px;
  border-left: 2px solid var(--conector);
}
/* Cada filho desenha o seu segmento vertical e o cotovelo ate o card.
   O ultimo segmento termina na ligacao, sem prolongar a linha para baixo. */
.md-typeset nav.arvore-hierarquia ul.arvore-filhos {
  margin-left: 12px; padding-left: 20px;
}
.md-typeset nav.arvore-hierarquia ul.arvore-filhos > li { padding-top: 16px; }
.arvore-hierarquia ul.arvore-filhos > li::before {
  content: ''; position: absolute; top: 0; bottom: 0; left: -20px;
  border-left: 2px solid var(--conector);
}
.arvore-hierarquia ul.arvore-filhos > li:last-child::before { bottom: auto; height: 38px; }
.arvore-hierarquia ul.arvore-filhos > li::after {
  content: ''; position: absolute; left: -20px; top: 38px; width: 20px;
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
/* Os ramos internos não podem ganhar mais recuo a cada geração.
   O nível inicial (raiz e seus quatro filhos) permanece intacto. */
.md-typeset nav.arvore-hierarquia ul.arvore-filhos > li > ul.arvore-filhos {
  position: relative;
  margin: 0;
  padding: 12px 0 0;
}
/* Liga o centro do card-pai ao trilho lateral dos filhos. */
.arvore-hierarquia ul.arvore-filhos > li > ul.arvore-filhos::before {
  content: '';
  position: absolute;
  top: 12px;
  left: -10px;
  width: calc(50% + 10px);
  border-top: 2px solid var(--conector);
}
.arvore-hierarquia ul.arvore-filhos > li > ul.arvore-filhos::after {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  height: 12px;
  border-left: 2px solid var(--conector);
}
/* Mantém os cards descendentes alinhados à coluna do pai. */
.arvore-hierarquia ul.arvore-filhos > li > ul.arvore-filhos > li::before {
  left: -10px;
}
.arvore-hierarquia ul.arvore-filhos > li > ul.arvore-filhos > li::after {
  left: -10px;
  width: 10px;
}
@media (max-width: 900px) {
  .arvore-hierarquia .arvore-raiz > .arvore-card { margin: 0; max-width: none; }
  .arvore-hierarquia .arvore-raiz > .arvore-card::after { display: none; }
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

CSS_ADICIONAL = """
<style>
.md-typeset nav.arvore-hierarquia ul.arvore-topo > li.arvore-raiz + li.arvore-raiz {
  margin-top: 32px;
}
.arvore-hierarquia .arvore-raiz:not(.arvore-com-filhos) > .arvore-card::after {
  display: none;
}
.arvore-novos {
  margin-top: 32px;
}
.arvore-novos h2 {
  font-size: 1.05rem;
  margin-bottom: 10px;
}
.arvore-novos-lista {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: 12px;
}
.arvore-novos-lista .arvore-card {
  display: flex;
  flex-direction: column;
  padding: 14px;
  gap: 8px;
  border: 1px dashed var(--md-default-fg-color--lightest);
  border-radius: 10px;
  text-decoration: none !important;
  color: inherit !important;
}
.arvore-novos-lista .arvore-card:hover {
  border-color: var(--md-primary-fg-color);
}
.arvore-novos-lista .arvore-card strong { font-size: 14px; }
.arvore-novos-lista .arvore-card span { font-size: 12px; opacity: .75; }
</style>
"""


def extrair_texto(texto: str) -> str:
    """Converte a formatação simples em texto legível no card."""
    texto = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", texto)
    texto = re.sub(r"<[^>]*>", "", texto)
    texto = re.sub(r"\\([\\`*_\[\]()#])", r"\1", texto)
    return texto.replace("**", "").replace("__", "").replace("`", "").strip()


def metadados_tutorial(arquivo: Path) -> tuple[str, str]:
    """Título do primeiro H1 e descrição do primeiro parágrafo do objetivo.

    Nenhuma configuração YAML é exigida no tutorial.
    """
    texto = arquivo.read_text(encoding="utf-8-sig")
    linhas = texto.splitlines()
    titulo = ""
    objetivo = ""
    primeiro_paragrafo = ""
    lendo_objetivo = False
    em_codigo = False
    for linha in linhas:
        t = linha.strip()
        if re.match(r"^(```+|~~~+)", t):
            em_codigo = not em_codigo
            continue
        if em_codigo or not t:
            continue
        h1 = re.match(r"^#\s+(.+?)\s*#*\s*$", t)
        if h1 and not titulo:
            titulo = extrair_texto(h1.group(1))
            continue
        h2 = re.match(r"^#{2,6}\s+(.+?)\s*$", t)
        if h2:
            lendo_objetivo = extrair_texto(h2.group(1)).casefold() == "objetivo"
            continue
        if re.match(r"^(?:\||[-*+]\s|\d+\.\s|>|<|---+$)", t):
            continue
        if lendo_objetivo and not objetivo:
            objetivo = extrair_texto(t)
        if titulo and not primeiro_paragrafo:
            primeiro_paragrafo = extrair_texto(t)

    if not titulo:
        raise ValueError(f"Falta o titulo '# ...' no tutorial: {arquivo}")
    descricao = objetivo or primeiro_paragrafo
    if len(descricao) > 190:
        descricao = descricao[:187].rstrip() + "..."
    return titulo, descricao


def carregar_materiais() -> dict[str, dict[str, str]]:
    arquivos = sorted(MATERIAIS.glob("*/*.md"), key=lambda p: p.as_posix().casefold())
    materiais = {}
    ids_normalizados = set()
    for arquivo in arquivos:
        identificador = f"{arquivo.parent.name}/{arquivo.stem}"
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*", identificador):
            raise ValueError(f"Nome do arquivo ou da pasta invalido: {arquivo}")
        if identificador.casefold() in ids_normalizados:
            raise ValueError(f"Tutorial duplicado (ignorando maiusculas): {identificador}")
        ids_normalizados.add(identificador.casefold())
        titulo, descricao = metadados_tutorial(arquivo)
        url = f"{PREFIXO}/materiais/{quote(arquivo.parent.name, safe='')}/{quote(arquivo.stem, safe='')}/"
        materiais[identificador] = {"titulo": titulo, "descricao": descricao, "url": url}
    return materiais


def carregar_roteiro(arquivo: Path, materiais: dict) -> tuple[list[dict], set[str]]:
    """Cada '- area/arquivo' é um card; dois espaços adicionam um filho."""
    raizes = []
    pilha = []
    encontrados = set()
    for numero, linha in enumerate(arquivo.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"( *)(?:- )([a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*)\s*", linha)
        if not match:
            raise ValueError(f"{arquivo}:{numero}: use somente '- area/arquivo', com 2 espacos para cada filho")
        nivel = len(match.group(1)) // 2
        if len(match.group(1)) % 2:
            raise ValueError(f"{arquivo}:{numero}: o recuo deve ter multiplo de 2 espacos")
        identificador = match.group(2)
        if identificador not in materiais:
            raise ValueError(f"{arquivo}:{numero}: tutorial inexistente '{identificador}'")
        if identificador in encontrados:
            raise ValueError(f"{arquivo}:{numero}: tutorial repetido na mesma arvore '{identificador}'")
        if nivel > len(pilha):
            raise ValueError(f"{arquivo}:{numero}: falta o card-pai acima de '{identificador}'")
        no = {"id": identificador, "filhos": []}
        if nivel == 0:
            raizes.append(no)
        else:
            pilha[nivel-1]["filhos"].append(no)
        pilha = pilha[:nivel] + [no]
        encontrados.add(identificador)
    return raizes, encontrados


def card(identificador: str, materiais: dict) -> str:
    dados = materiais[identificador]
    descricao = f'<span>{escape(dados["descricao"])}</span>' if dados["descricao"] else ""
    return (
        f'<a class="arvore-card" href="{escape(dados["url"], quote=True)}">'
        f'<strong>{escape(dados["titulo"])}</strong>{descricao}</a>'
    )


def renderizar_arvore(raizes: list[dict], materiais: dict) -> str:
    def renderizar(no: dict, raiz=False) -> str:
        classe = ' class="arvore-raiz arvore-com-filhos"' if raiz and no["filhos"] else (' class="arvore-raiz"' if raiz else '')
        conteudo = [f'<li{classe} data-id="{escape(no["id"], quote=True)}">', card(no["id"], materiais)]
        if no["filhos"]:
            conteudo.append('<ul class="arvore-filhos">')
            conteudo.extend(renderizar(filho) for filho in no["filhos"])
            conteudo.append('</ul>')
        conteudo.append('</li>')
        return "\n".join(conteudo)

    if not raizes:
        return "<p>Esta trilha ainda nao possui tutoriais no roteiro.</p>"
    return ('<nav class="arvore-hierarquia" aria-label="Árvore dos materiais">\n'
            '<ul class="arvore-topo">\n'
            + "\n".join(renderizar(no, raiz=True) for no in raizes)
            + '\n</ul>\n</nav>')


def renderizar_novos(ids: list[str], materiais: dict) -> str:
    if not ids:
        return ""
    return ('<section class="arvore-novos">\n'
            '<h2>Novos tutoriais</h2>\n'
            '<p>Materiais desta área que ainda não foram posicionados na árvore.</p>\n'
            '<div class="arvore-novos-lista">\n'
            + "\n".join(card(i, materiais) for i in ids)
            + '\n</div>\n</section>')


def processar_trilha(arquivo_roteiro: Path, materiais: dict) -> int:
    slug = arquivo_roteiro.stem
    trilha = TRILHAS / slug
    if not trilha.is_dir():
        # Mantém a pasta Web existente com maiúscula sem duplicá-la no Git.
        equivalentes = [p for p in TRILHAS.iterdir() if p.is_dir() and p.name.casefold() == slug.casefold()]
        if len(equivalentes) != 1:
            raise ValueError(f"Nao foi encontrada uma unica trilha para o roteiro '{slug}'")
        trilha = equivalentes[0]
    destino = trilha / "conteudo.md"
    if not (trilha / "index.md").is_file() or not destino.is_file():
        raise ValueError(f"Roteiro '{arquivo_roteiro}' sem trilha completa: index.md e conteudo.md em {trilha}")
    texto = destino.read_text(encoding="utf-8")
    if texto.count(MARCADOR) != 1:
        raise ValueError(f"A trilha {trilha} precisa ter exatamente um marcador GERAR_CARDS")
    raizes, usados = carregar_roteiro(arquivo_roteiro, materiais)
    outros = sorted(
        (i for i in materiais if i.startswith(slug + "/") and i not in usados),
        key=lambda i: materiais[i]["titulo"].casefold()
    )
    arvore = renderizar_arvore(raizes, materiais)
    arvore += "\n" + renderizar_novos(outros, materiais)
    arvore += "\n" + CSS_HIERARQUIA + "\n" + CSS_ADICIONAL
    destino.write_text(texto.replace(MARCADOR, arvore, 1), encoding="utf-8")
    print(f"{slug}: {len(usados)} cards na arvore, {len(outros)} novos")
    return len(usados)


def redirecionar_links_antigos(materiais: dict) -> None:
    """Conserva URLs anteriores no site gerado, sem pastas antigas no Git."""
    mapa = Path("scripts/redirecionamentos_antigos.json")
    if not mapa.exists():
        return
    antigos = json.loads(mapa.read_text(encoding="utf-8"))
    for caminho_antigo, identificador in antigos.items():
        if identificador not in materiais:
            raise ValueError(f"Redirecionamento para tutorial inexistente: {identificador}")
        partes = caminho_antigo.split("/")
        if len(partes) != 2 or not all(re.fullmatch(r"[a-z0-9][a-z0-9-]*", parte) for parte in partes):
            raise ValueError(f"Identificador antigo invalido: {caminho_antigo}")
        url = materiais[identificador]["url"]
        diretorio = TRILHAS / partes[0] / "materiais" / partes[1]
        diretorio.mkdir(parents=True, exist_ok=True)
        # Javascript redireciona automaticamente, com link acessivel como fallback.
        conteudo = (
            '# Tutorial transferido\n\n'
            f'Este material foi movido para [seu novo endereço]({url}).\n\n'
            f'<meta http-equiv="refresh" content="0; url={escape(url, quote=True)}">\n'
            f'<script>window.location.replace({json.dumps(url)});</script>\n'
        )
        (diretorio / "index.md").write_text(conteudo, encoding="utf-8")
        (diretorio / "conteudo.md").write_text(conteudo, encoding="utf-8")
    print(f"URLs antigas preservadas: {len(antigos)} tutoriais")


def main() -> None:
    materiais = carregar_materiais()
    if not materiais:
        raise ValueError(f"Nenhum tutorial encontrado em {MATERIAIS}")
    usados = 0
    for roteiro in sorted(ROTEIROS.glob("*.md")):
        usados += processar_trilha(roteiro, materiais)
    categorias = sorted({i.split("/")[0] for i in materiais})
    sem_trilha = [cat for cat in categorias if not (ROTEIROS / f"{cat}.md").is_file()]
    if sem_trilha:
        raise ValueError(f"Areas com tutoriais mas sem trilha/roteiro: {', '.join(sem_trilha)}")
    redirecionar_links_antigos(materiais)
    print(f"Total: {len(materiais)} tutoriais individuais / {usados} referencias em arvores")


if __name__ == "__main__":
    main()
