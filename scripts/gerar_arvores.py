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
