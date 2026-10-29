from pathlib import Path
from collections import defaultdict
from html import escape
from urllib.parse import quote, urlsplit
import re
import yaml

ROOT = Path("docs/trilhas/tutoriais")
MARCADOR = "<!-- GERAR_CARDS -->"


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

    link = (
        f"/LDTT_Capacitacao/trilhas/tutoriais/"
        f"{trilha}/materiais/{tutorial}/"
    )

    if caminho_site:
        link += f"{caminho_site}/"

    return link, False



def gerar_card(arquivo, dados):
    titulo = dados.get("title")
    descricao = dados.get("description")
    nivel = dados.get("nivel")
    destino = dados.get("destino")

    if not isinstance(titulo, str) or not titulo.strip():
        raise ValueError("title invalido")

    if not isinstance(descricao, str):
        raise ValueError("description invalida")

    if type(nivel) is not int or nivel < 0:
        raise ValueError("nivel deve ser um inteiro >= 0")

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

    return nivel, ordem, card


CSS = """
<style>
.ldtt-arvore {
  width: 100%;
  margin: 24px 0;
}

.arvore-nivel {
  text-align: center;
}

.arvore-rotulo {
  display: block;
  font-size: 12px;
  opacity: 0.65;
  margin-bottom: 8px;
}

.arvore-linha {
  display: flex;
  justify-content: center;
  gap: 20px;
  padding: 8px 4px;
  overflow-x: auto;
}

.arvore-card {
  position: relative;
  display: flex;
  flex-direction: column;
  flex: 0 0 200px;
  gap: 8px;
  min-height: 95px;
  padding: 14px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 10px;
  color: inherit !important;
  text-decoration: none !important;
  text-align: left;
  transition: border-color 0.2s;
}

.arvore-card:hover {
  border-color: var(--md-primary-fg-color);
}

.arvore-card strong {
  font-size: 14px;
}

.arvore-card span {
  font-size: 12px;
  opacity: 0.7;
}

.arvore-card + .arvore-card::before {
  content: "";
  position: absolute;
  left: -21px;
  top: 50%;
  width: 20px;
  border-top: 2px solid var(--md-default-fg-color--lightest);
}

.arvore-conector {
  height: 35px;
  width: 2px;
  margin: 0 auto;
  background: var(--md-default-fg-color--lightest);
}

@media (max-width: 600px) {
  .arvore-linha {
    justify-content: flex-start;
  }

  .arvore-card {
    flex-basis: 180px;
  }
}
</style>
"""



def montar_arvore(grupos):
    if not grupos:
        return "<p>Nenhum tutorial cadastrado ainda.</p>"

    partes = ['<div class="ldtt-arvore">']

    niveis = sorted(grupos)

    for indice, nivel in enumerate(niveis):
        partes.append("""
<div class="arvore-nivel">
  <div class="arvore-linha">
""")

        for _, _, card in sorted(grupos[nivel]):
            partes.append(card)

        partes.append("""
  </div>
</div>
""")

        if indice < len(niveis) - 1:
            partes.append(
                '<div class="arvore-conector" aria-hidden="true"></div>'
            )

    partes.append("</div>")
    partes.append(CSS)

    return "\n".join(partes)



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


def montar_hierarquia(nos):
    """Valida pais e niveis antes de gerar uma lista aninhada de materiais."""
    filhos = defaultdict(list)
    for identificador, no in nos.items():
        if "pai" not in no:
            raise ValueError(f"Informe pai (ou null na raiz): {identificador}")
        pai = no["pai"]
        if pai is not None and (not isinstance(pai, str) or pai not in nos):
            raise ValueError(f"Pai inexistente ou invalido: {identificador}")
        filhos[pai].append(identificador)

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

    for identificador, no in nos.items():
        if no["nivel"] != profundidade(identificador):
            raise ValueError(f"Nivel incompativel com o pai: {identificador}")
    if len(filhos[None]) != 1:
        raise ValueError("A arvore deve ter uma unica raiz de nivel 0")

    def renderizar(pai):
        partes = ['<ul class="arvore-filhos">' if pai is not None else '<ul class="arvore-topo">']
        for identificador in sorted(filhos[pai], key=lambda item: (nos[item]["ordem"], item)):
            no = nos[identificador]
            classe = ' class="arvore-raiz"' if pai is None else ''
            partes.append(f'<li{classe} data-id="{escape(identificador, quote=True)}" data-nivel="{no["nivel"]}">')
            partes.append(no["card"])
            if filhos[identificador]:
                partes.append(renderizar(identificador))
            partes.append('</li>')
        partes.append('</ul>')
        return '\n'.join(partes)

    return '<nav class="arvore-hierarquia" aria-label="Árvore dos materiais">\n' + renderizar(None) + '\n</nav>\n' + CSS_HIERARQUIA


def processar_trilha(trilha):
    arquivo_index = trilha / "index.md"
    arquivo_conteudo = trilha / "conteudo.md"
    pasta_materiais = trilha / "materiais"

    if not arquivo_index.is_file():
        return

    # A trilha precisa ter uma página de conteúdo.
    if not arquivo_conteudo.is_file():
        print(f"AVISO: {trilha.name} sem conteudo.md")
        return

    texto_original = arquivo_conteudo.read_text(encoding="utf-8")

    # Preserva todo o conteúdo caso não exista o marcador.
    if MARCADOR not in texto_original:
        print(f"AVISO: {trilha.name} sem marcador GERAR_CARDS")
        return

    grupos = defaultdict(list)
    nos = {}
    hierarquica = False

    if pasta_materiais.exists():
        arquivos = sorted(
            pasta_materiais.glob("*/index.md"),
            key=lambda p: p.parent.name.lower()
        )

       
        for arquivo in arquivos:
            try:
                dados = ler_metadados(arquivo)
                nivel, ordem, card = gerar_card(arquivo, dados)
                no = dict(nivel=nivel, ordem=ordem, card=card)
                if "pai" in dados:
                    hierarquica = True
                    no["pai"] = dados["pai"]
                nos[arquivo.parent.name] = no

                grupos[nivel].append(
                    (ordem, arquivo.parent.name.lower(), card)
                )

            except (ValueError, yaml.YAMLError) as erro:
                print(f"AVISO: {arquivo}: {erro}")


    arvore = montar_hierarquia(nos) if hierarquica else montar_arvore(grupos)

    # Substitui somente o marcador.
    texto_final = texto_original.replace(MARCADOR, arvore, 1)

    # Altera o arquivo apenas no ambiente temporário do build.
    arquivo_conteudo.write_text(
        texto_final,
        encoding="utf-8"
    )

    total = sum(len(cards) for cards in grupos.values())

    print(
        f"{trilha.name}: {total} tutoriais "
        f"em {len(grupos)} niveis"
    )


if __name__ == "__main__" and ROOT.exists():
    for trilha in sorted(
        ROOT.iterdir(),
        key=lambda p: p.name.lower()
    ):
        if trilha.is_dir():
            processar_trilha(trilha)
