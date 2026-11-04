// Atualiza páginas restauradas pelo histórico com a paleta escolhida depois.
// O Zensical persiste a escolha, mas uma página no cache mantém seu DOM antigo.
window.addEventListener("pageshow", (evento) => {
  if (!evento.persisted || typeof __md_get !== "function") return;

  let paleta;
  try {
    paleta = __md_get("__palette");
  } catch {
    return;
  }

  const opcoes = document.querySelectorAll(
    '[data-md-component="palette"] input[name="__palette"]'
  );
  const indice = paleta?.index;
  if (!Number.isInteger(indice) || indice < 0 || indice >= opcoes.length) return;

  const opcao = opcoes[indice];
  if (document.body.dataset.mdColorScheme === opcao.dataset.mdColorScheme) return;

  opcao.checked = true;
  opcao.dispatchEvent(new Event("change", { bubbles: true }));
});
