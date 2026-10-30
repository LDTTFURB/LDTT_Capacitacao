from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

DOCS = Path("docs")
CODIGO = re.compile(r"^```.*?^```|`[^`\n]*`", re.DOTALL | re.MULTILINE)
LINK = re.compile(r"\]\(\s*<?([^)\s>]+)")


def links_quebrados(arquivo):
    # Exemplos dentro de blocos de codigo nao sao links de verdade.
    texto = CODIGO.sub("", arquivo.read_text(encoding="utf-8-sig"))

    for destino in LINK.findall(texto):
        url = urlsplit(destino)

        if url.scheme or url.netloc or not url.path or url.path.startswith("/"):
            continue

        if not (arquivo.parent / unquote(url.path)).exists():
            yield destino


quebrados = [
    f"{arquivo}: {destino}"
    for arquivo in sorted(DOCS.rglob("*.md"))
    for destino in links_quebrados(arquivo)
]

for quebrado in quebrados:
    print(f"ERRO: link quebrado em {quebrado}")

sys.exit(1 if quebrados else 0)
