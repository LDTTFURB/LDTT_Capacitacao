(() => {
  function iniciarFiltro() {
    const busca = document.getElementById("trilhas-busca");
    const lista = document.getElementById("trilhas-cards");
    const mensagem = document.getElementById("trilhas-sem-resultados");
    if (!busca || !lista || !mensagem || busca.dataset.filtroAtivo) return;
    busca.dataset.filtroAtivo = "true";

    const cards = lista.querySelectorAll("[data-tag]");
    function filtrar() {
      const tag = busca.value.trim().toLowerCase();
      let encontrados = 0;
      cards.forEach((card) => {
        const visivel = !tag || card.dataset.tag.toLowerCase() === tag;
        card.hidden = !visivel;
        card.style.display = visivel ? "" : "none";
        if (visivel) encontrados++;
      });
      lista.hidden = encontrados === 0;
      lista.style.display = encontrados ? "" : "none";
      mensagem.hidden = encontrados > 0;
    }

    busca.addEventListener("input", filtrar);
    filtrar();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", iniciarFiltro);
  } else {
    iniciarFiltro();
  }
  if (typeof document$ !== "undefined") document$.subscribe(iniciarFiltro);
})();
