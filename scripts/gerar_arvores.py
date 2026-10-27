
from pathlib import Path
from collections import defaultdict
from html import escape
from urllib.parse import quote, urlsplit
import re
import yaml

ROOT = Path("docs/trilhas/tutoriais")

CSS = """
<style>
.arvore {
  width: 100%;
  text-align: center;
}
.arvore-rotulo {
  display: block;
  font-size: 12px;
  opacity: .65;
  margin-bottom: 8px;
}
.arvore-linha {
  display: flex;
  justify-content: center;
  gap: 20px;
  overflow-x: auto;
  padding: 8px 4px;
}
.arvore-card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 0 0 210px;
  padding: 14px;
  min-height: 95px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 10px;
  color: inherit !important;
  text-decoration: none !important;
  text-align: left;
}
.arvore-card:hover {
  border-color: var(--md-primary-fg-color);
}
.arvore-card strong {
  font-size: 14px;
}
.arvore-card span {
  font-size: 12px;
  opacity: .7;
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
  width: 2px;
  height: 35px;
  background: var(--md-default-fg-color--lightest);
  margin: 0 auto;
}
@media (max-width: 600px) {
  .arvore-linha {
    flex-direction: column;
    align-items: center;
    overflow: visible;
  }
  .arvore-card {
    flex: none;
    width: min(100%, 300px);
  }
  .arvore-card + .arvore-card::before {
    display: none;
  }
}
</style>
"""


def ler_metadados(arquivo):
    texto = arquivo.read_text(encoding="utf-8-sig").lstrip()

    resultado = re.match(
        r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)",
        texto,
        re.DOTALL
    )

    if not resultado:
        raise ValueError(f"Metadados ausentes: {arquivo}")

    dados = yaml.safe_load(resultado.group(1))

    if not isinstance(dados, dict):
        raise ValueError(f"Metadados invalidos: {arquivo}")

    cabecalho = texto[:resultado.end()].rstrip()
    return dados, cabecalho


def obter_destino(arquivo, destino):
    url = urlsplit(destino)

    if url.scheme in ("http", "https") and url.netloc:
        return destino, True

    if url.scheme or url.netloc:
        raise ValueError("URL externa invalida")

    caminho = Path(destino)

    if (caminho.is_absolute()
        or ".." in caminho.parts
        or caminho.suffix.lower() != ".md"):
        raise ValueError("Destino deve ser um arquivo .md relativo")

    if not (arquivo.parent / caminho).is_file():
        raise ValueError(f"Arquivo de destino inexistente: {destino}")

    relativo = caminho.with_suffix("")

    if caminho.stem == "index":
        relativo = caminho.parent

    pasta = quote(arquivo.parent.name)
    pagina = relativo.as_posix()

    link = f"materiais/{pasta}/"

    if pagina != ".":
        link += quote(pagina, safe="/") + "/"

    return link, False


def gerar_arvore(trilha):
    raiz = trilha / "index.md"

    if not raiz.is_file():
        return

    arquivos = sorted(
        (trilha / "materiais").glob("*/index.md")
    )

    if not arquivos:
        return

    grupos = defaultdict(list)

    for arquivo in arquivos:
        try:
            dados, _ = ler_metadados(arquivo)

            titulo = dados.get("title")
            descricao = dados.get("description")
            nivel = dados.get("nivel")
            destino = dados.get("destino")

            if not isinstance(titulo, str) or not titulo.strip():
                raise ValueError("title invalido")

            if not isinstance(descricao, str):
                raise ValueError("description invalida")

            if type(nivel) is not int or nivel < 0:
                raise ValueError("nivel deve ser inteiro >= 0")

            if not isinstance(destino, str) or not destino.strip():
                raise ValueError("destino invalido")

            link, externo = obter_destino(arquivo, destino.strip())

            extra = ' target="_blank" rel="noopener noreferrer"' if externo else ""

            card = (
                f'<a class="arvore-card" href="{escape(link, quote=True)}"{extra}>'
                f'<strong>{escape(titulo)}</strong>'
                f'<span>{escape(descricao)}</span>'
                '</a>'
            )

            grupos[nivel].append((titulo.lower(), card))

        except (ValueError, yaml.YAMLError) as erro:
            print(f"AVISO: {arquivo}: {erro}")

    if not grupos:
        print(f"Nenhum tutorial valido em {trilha.name}")
        return

    info, cabecalho = ler_metadados(raiz)
    nome = str(info.get("title") or trilha.name)

    partes = [
        cabecalho,
        f"# {escape(nome)}",
        '<div class="arvore">'
    ]

    niveis = sorted(grupos)

    for indice, nivel in enumerate(niveis):
        partes.append(
            f'<div class="arvore-nivel">'
            f'<small class="arvore-rotulo">Nível {nivel}</small>'
            '<div class="arvore-linha">'
        )

        for _, card in sorted(grupos[nivel]):
            partes.append(card)

        partes.append("</div></div>")

        if indice < len(niveis) - 1:
            partes.append(
                '<div class="arvore-conector" aria-hidden="true"></div>'
            )

    partes.extend(["</div>", CSS])

    raiz.write_text(
        "\n\n".join(partes) + "\n",
        encoding="utf-8"
    )

    total = sum(len(grupo) for grupo in grupos.values())
    print(f"{trilha.name}: {total} tutoriais em {len(niveis)} niveis")


for trilha in sorted(ROOT.iterdir()):
    if trilha.is_dir():
        gerar_arvore(trilha)
