
from pathlib import Path
from html import escape
from urllib.parse import quote
import yaml

BASE = Path("docs/trilhas")
TUTORIAIS = BASE / "tutoriais"
DESTINO = BASE / "index.md"

cards = []

for arquivo in sorted(TUTORIAIS.glob("*/index.md")):
    texto = arquivo.read_text(encoding="utf-8")
    texto = texto.lstrip("\ufeff \t\r\n")

    if not texto.startswith("---\n"):
        raise ValueError(f"Metadados ausentes: {arquivo}")

    partes = texto.split("---", 2)
    dados = yaml.safe_load(partes[1])

    titulo = dados.get("title")
    descricao = dados.get("description")
    tags = dados.get("tags")

    if (not isinstance(titulo, str)
        or not isinstance(descricao, str)
        or not isinstance(tags, list)
        or not tags
        or not all(isinstance(t, str) for t in tags)):
        raise ValueError(f"Metadados invalidos: {arquivo}")

    pasta = quote(arquivo.parent.name)
    nomes_tags = ", ".join(tags)

    cards.append(f"""
<a class="ldtt-card" href="tutoriais/{pasta}/"
   data-tags="{escape(','.join(tags), quote=True)}">
  <strong>{escape(titulo)}</strong>
  <span>{escape(descricao)}</span>
  <small>{escape(nomes_tags)}</small>
</a>
""")

# Mantenha daqui para baixo o código existente:
# pagina = ...
