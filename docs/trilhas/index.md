
# Trilhas

Explore tutoriais e materiais de capacitação do LDTT.

<input
  id="trilhas-busca"
  type="search"
  placeholder="Buscar por tag..."
  aria-label="Buscar por tag"
/>

<!--
Para adicionar outro card:
Copie um bloco <a>, altere o link (href),
o nome, a descrição e a tag (data-tag).
-->

<div id="trilhas-cards" class="ldtt-grid">

  <a class="ldtt-card"
     href="https://learn.unity.com/"
     data-tag="Unity">
    <strong>Unity Learn</strong>
    <span>Materiais introdutórios da Unity.</span>
    <small>Unity</small>
  </a>

  <a class="ldtt-card"
     href="https://developer.mozilla.org/pt-BR/docs/Learn_web_development"
     data-tag="Web">
    <strong>HTML e CSS</strong>
    <span>Fundamentos de desenvolvimento Web.</span>
    <small>Web</small>
  </a>

  <a class="ldtt-card"
     href="https://docs.python.org/pt-br/3/tutorial/"
     data-tag="Python">
    <strong>Python</strong>
    <span>Introdução à programação Python.</span>
    <small>Python</small>
  </a>

</div>

<p id="trilhas-sem-resultados" hidden>
  Nenhum tutorial encontrado.
</p>

<style>
#trilhas-busca {
  width: 100%;
  padding: 10px 12px;
  margin: 12px 0;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
}

.ldtt-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin-top: 18px;
}

.ldtt-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-height: 115px;
  padding: 14px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 10px;
  color: var(--md-default-fg-color) !important;
  text-decoration: none !important;
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
  font-size: 11px;
  color: var(--md-primary-fg-color);
}

@media (max-width: 900px) {
  .ldtt-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 580px) {
  .ldtt-grid {
    grid-template-columns: 1fr;
  }
}
</style>
