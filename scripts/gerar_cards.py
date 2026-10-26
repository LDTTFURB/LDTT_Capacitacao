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

pagina = """---
hide:
  - navigation
  - toc
---

# Trilhas de Capacitação

Explore os tutoriais do LDTT.

<input id="busca-tag" type="search"
       placeholder="Buscar por tag...">

<div class="ldtt-grid">
""" + "\n".join(cards) + """
</div>

<p id="sem-resultados" hidden>Nenhum tutorial encontrado.</p>

<style>
#busca-tag {
  width: 100%;
  padding: 10px;
  margin: 12px 0 20px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
}

.ldtt-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}

.ldtt-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 14px;
  min-height: 110px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 10px;
  color: inherit !important;
  text-decoration: none !important;
}

.ldtt-card:hover {
  border-color: var(--md-primary-fg-color);
}

.ldtt-card strong { font-size: 15px; }
.ldtt-card span { font-size: 12px; }

.ldtt-card small {
  margin-top: auto;
  color: var(--md-primary-fg-color);
}

.ldtt-card[hidden],
#sem-resultados[hidden] {
  display: none !important;
}

@media (max-width: 700px) {
  .ldtt-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 450px) {
  .ldtt-grid { grid-template-columns: 1fr; }
}
</style>

<script>
(() => {
  const campo = document.getElementById("busca-tag");
  const cards = document.querySelectorAll(".ldtt-card");
  const vazio = document.getElementById("sem-resultados");

  function filtrar() {
    const busca = campo.value.trim().toLowerCase();
    let encontrados = 0;

    cards.forEach(card => {
      const tags = (card.dataset.tags || "").toLowerCase();
      const mostrar = tags.split(",").some(
        tag => tag.trim().includes(busca)
      );

      card.hidden = !mostrar;
      if (mostrar) encontrados++;
    });

    vazio.hidden = encontrados > 0;
  }

  campo.addEventListener("input", filtrar);
  filtrar();
})();
</script>
"""

DESTINO.write_text(pagina, encoding="utf-8")
print(f"Cards gerados: {len(cards)}")

