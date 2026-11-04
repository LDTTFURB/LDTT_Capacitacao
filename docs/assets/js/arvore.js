// Em telas estreitas, abre a árvore com o card raiz no centro da área visível.
function centralizarArvores() {
  document.querySelectorAll(".arvore-hierarquia").forEach((arvore) => {
    if (arvore.dataset.centralizada || arvore.scrollWidth <= arvore.clientWidth) return;

    const raiz = arvore.querySelector(".arvore-raiz > .arvore-card");
    if (!raiz) return;
    const card = raiz.getBoundingClientRect();
    const area = arvore.getBoundingClientRect();
    arvore.scrollLeft += card.left - area.left + card.width / 2 - area.width / 2;
    arvore.dataset.centralizada = "true";
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", centralizarArvores);
} else {
  centralizarArvores();
}
if (typeof document$ !== "undefined") document$.subscribe(centralizarArvores);
window.addEventListener("resize", centralizarArvores);
