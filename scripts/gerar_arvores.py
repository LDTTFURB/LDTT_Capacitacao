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
        partes.append(f"""
<div class="arvore-nivel">
  <small class="arvore-rotulo">Nível {nivel}</small>
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

    if pasta_materiais.exists():
        arquivos = sorted(
            pasta_materiais.glob("*/index.md"),
            key=lambda p: p.parent.name.lower()
        )

        for arquivo in arquivos:
            try:
                dados = ler_metadados(arquivo)
                nivel, ordem, card = gerar_card(arquivo, dados)

                grupos[nivel].append(
                (ordem, arquivo.parent.name.lower(), card)
        )

            except (ValueError, yaml.YAMLError) as erro:
                print(f"AVISO: {arquivo}: {erro}")

    arvore = montar_arvore(grupos)

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


if ROOT.exists():
    for trilha in sorted(
        ROOT.iterdir(),
        key=lambda p: p.name.lower()
    ):
        if trilha.is_dir():
            processar_trilha(trilha)
