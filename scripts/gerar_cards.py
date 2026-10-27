
from pathlib import Path
from html import escape
from urllib.parse import quote
import re
import yaml

BASE = Path("docs/trilhas")
TUTORIAIS = BASE / "tutoriais"
DESTINO = BASE / "index.md"


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


cards = []

if TUTORIAIS.exists():
    arquivos = sorted(
        TUTORIAIS.glob("*/index.md"),
        key=lambda p: p.parent.name.lower()
    )

    for arquivo in arquivos:
        try:
            dados = ler_metadados(arquivo)

            titulo = dados.get("title")
            descricao = dados.get("description")
            tags = dados.get("tags")

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

            pasta = quote(arquivo.parent.name, safe="")

            # Novo formato: abre conteudo.md.
            # Compatibilidade com trilhas antigas: abre index.md.
            if (arquivo.parent / "conteudo.md").exists():
                link = f"tutoriais/{pasta}/conteudo/"
            else:
                link = f"tutoriais/{pasta}/"

            nomes_tags = ", ".join(tags)

            cards.append(f"""
<a class="ldtt-card"
   href="{escape(link, quote=True)}"
   data-tags="{escape(nomes_tags, quote=True)}">
  <strong>{escape(titulo)}</strong>
  <span>{escape(descricao)}</span>
  <small>{escape(nomes_tags)}</small>
</a>
""")

        except (ValueError, yaml.YAMLError) as erro:
            print(f"AVISO: {arquivo}: {erro}")


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
  transition: border-color 0.2s;
}

.ldtt-card:hover {
  border-color: var(--md-primary-fg-color);
}

.ldtt-card strong {
  font-size: 15px;
}

.ldtt-card span {
  font-size: 12px;
  color: var(--md-default-fg-color--light);
}

.ldtt-card small {
  margin-top: auto;
  color: var(--md-primary-fg-color);
  font-size: 11px;
}

.ldtt-card[hidden],
#sem-resultados[hidden] {
  display: none !important;
}

@media (max-width: 900px) {
  .ldtt-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 580px) {
  .ldtt-grid {
    grid-template-columns: 1fr;
  }
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

      const mostrar = !termo || tags.some(
        tag => tag.trim().includes(termo)
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

DESTINO.parent.mkdir(parents=True, exist_ok=True)
DESTINO.write_text(pagina, encoding="utf-8")

print(f"Cards gerados: {len(cards)}")
