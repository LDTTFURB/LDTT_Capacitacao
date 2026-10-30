
from pathlib import Path

from gerar_arvores import gerar_card_trilha, ler_trilhas

BASE = Path("docs/trilhas")
DESTINO = BASE / "index.md"


# Subtrilhas ficam dentro da trilha-mae, mas continuam sendo achadas pela busca.
cards = [
    gerar_card_trilha(pasta, dados, subtrilha=bool(dados.get("pai")))
    for pasta, dados in ler_trilhas().items()
]


pagina = """---
hide:
  - navigation
  - toc
---

# Trilhas de Capacitação

Explore os tutoriais desenvolvidos pelo LDTT.

<input
  id="busca-tag"
  type="search"
  placeholder="Buscar por tag..."
  aria-label="Buscar por tag"
/>

<div class="ldtt-grid">
"""

pagina += "\n".join(cards)

pagina += """
</div>

<p id="sem-resultados" hidden>
  Nenhuma trilha encontrada.
</p>

<style>
#busca-tag {
  width: 100%;
  padding: 10px 12px;
  margin: 12px 0 20px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
}

.ldtt-card[hidden],
#sem-resultados[hidden] {
  display: none !important;
}
</style>

<script>
(() => {
  const campo = document.getElementById("busca-tag");
  const cards = [...document.querySelectorAll(".ldtt-card")];
  const vazio = document.getElementById("sem-resultados");

  if (!campo || !vazio) return;

  function filtrar() {
    const termo = campo.value.trim().toLowerCase();
    let encontrados = 0;

    cards.forEach(card => {
      const tags = (card.dataset.tags || "")
        .toLowerCase()
        .split(",");

      const mostrar = termo
        ? tags.some(tag => tag.trim().includes(termo))
        : !card.hasAttribute("data-subtrilha");

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

DESTINO.parent.mkdir(parents=True, exist_ok=True)
DESTINO.write_text(pagina, encoding="utf-8")

print(f"Cards gerados: {len(cards)}")
