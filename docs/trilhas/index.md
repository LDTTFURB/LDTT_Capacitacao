---
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

<a class="ldtt-card"
   href="tutoriais/boas-praticas/conteudo/"
   data-tags="Boas práticas, Organização, Equipe">
  <strong>Boas práticas</strong>
  <span>Organização de arquivos, convenções e rotina de desenvolvimento.</span>
  <small>Boas práticas, Organização, Equipe</small>
</a>


<a class="ldtt-card"
   href="tutoriais/como-criar-tutorial/conteudo/"
   data-tags="Tutorial, GitHub">
  <strong>Como criar um tutorial</strong>
  <span>Aprenda a criar e publicar tutoriais no HUB do LDTT.</span>
  <small>Tutorial, GitHub</small>
</a>


<a class="ldtt-card"
   href="tutoriais/csharp/conteudo/"
   data-tags="CSharp, Programação, Unity">
  <strong>Programação C#</strong>
  <span>Aprenda C#, eventos, refatoração e padrões de projeto.</span>
  <small>CSharp, Programação, Unity</small>
</a>


<a class="ldtt-card"
   href="tutoriais/eletronica/conteudo/"
   data-tags="Eletrônica">
  <strong>Eletrônica</strong>
  <span>Tutoriais de Eletrônica.</span>
  <small>Eletrônica</small>
</a>


<a class="ldtt-card"
   href="tutoriais/git/conteudo/"
   data-tags="Git, GitHub, Versionamento">
  <strong>Git e GitHub</strong>
  <span>Aprenda versionamento, branches, commits e revisão de código.</span>
  <small>Git, GitHub, Versionamento</small>
</a>


<a class="ldtt-card"
   href="tutoriais/unity/conteudo/"
   data-tags="Unity, Jogos, CSharp">
  <strong>Unity</strong>
  <span>Aprenda Unity e encontre tutoriais relacionados de Git, C# e boas práticas.</span>
  <small>Unity, Jogos, CSharp</small>
</a>


<a class="ldtt-card"
   href="tutoriais/vr/conteudo/"
   data-tags="VR, Unity, Google Cardboard, Meta Quest">
  <strong>Realidade Virtual (VR)</strong>
  <span>Crie e teste aplicações de VR na Unity para Google Cardboard e Meta Quest.</span>
  <small>VR, Unity, Google Cardboard, Meta Quest</small>
</a>


<a class="ldtt-card"
   href="tutoriais/Web/conteudo/"
   data-tags="Web">
  <strong>Web</strong>
  <span>Tutoriais de WEB.</span>
  <small>Web</small>
</a>

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
