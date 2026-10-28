
## Como gerar os cards dentro de uma trilha

Para mostrar os tutoriais cadastrados dentro de uma
trilha, utilizamos o marcador:

`<!-- GERAR_CARDS -->`

### 1. Adicione o marcador

No arquivo `conteudo.md` da trilha, coloque o marcador
onde deseja que os cards apareçam.

Exemplo:

# Unity

Bem-vindo à trilha Unity!

Aqui você encontrará materiais para começar.

## Tutoriais

<!-- GERAR_CARDS -->

## Informações adicionais

Outras informações podem ser escritas aqui.

### 2. Como funciona?

O HUB procura automaticamente os tutoriais dentro
da pasta `materiais/` da trilha.

Cada tutorial encontrado é organizado de acordo
com os campos `nivel` e `ordem` do seu `index.md`.

O sistema gera os cards no lugar do marcador,
sem precisar escrever HTML ou editar scripts.

### 3. Resultado

Se a pasta `materiais/` possuir três tutoriais:

- Fundamentos Unity (nível 0)
- Fundamentos Programação (nível 0)
- Configurar Build Android (nível 1)

Os dois primeiros aparecerão lado a lado, e o
terceiro aparecerá abaixo, conectado aos anteriores.

### Importante

- Utilize apenas um `<!-- GERAR_CARDS -->` por trilha.
- Você pode escrever textos, adicionar imagens e links
  antes ou depois do marcador.
- Não é necessário criar os cards manualmente.
- Novos tutoriais aparecerão automaticamente após
  a publicação pelo GitHub Actions.
