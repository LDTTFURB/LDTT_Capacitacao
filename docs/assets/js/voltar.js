
document.addEventListener("DOMContentLoaded", () => {
  const base = "/LDTT_Capacitacao/";
  const atual = window.location.pathname;

  // Não mostra o botão na página inicial.
  if (atual === base || atual === base + "index.html") {
    return;
  }

  const conteudo = document.querySelector(".md-content__inner");

  if (!conteudo || document.querySelector(".ldtt-voltar")) {
    return;
  }

  const trilhas = base + "trilhas/";
  let destino = base;

  if (atual.startsWith(trilhas)) {
    destino = trilhas;
  }

  // Dentro de um tutorial, voltar para a trilha.
  const partes = atual.match(
    /\/trilhas\/tutoriais\/([^/]+)\/materiais\//
  );

  if (partes) {
    destino = base + "trilhas/tutoriais/" +
      partes[1] + "/conteudo/";
  }

  const botao = document.createElement("a");
  botao.className = "ldtt-voltar";
  botao.href = destino;
  botao.textContent = "← Voltar";

  botao.addEventListener("click", (evento) => {
    const anterior = document.referrer;

    // Volta à página anterior se ela pertence ao HUB.
    if (
      anterior &&
      anterior.startsWith(window.location.origin + base) &&
      anterior !== window.location.href
    ) {
      evento.preventDefault();
      window.history.back();
    }
  });

  conteudo.prepend(botao);
});
