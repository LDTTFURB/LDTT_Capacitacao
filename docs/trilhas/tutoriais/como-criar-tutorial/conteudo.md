
# Como criar um tutorial

Para compartilhar um material no HUB do LDTT,
basta criar uma pasta com dois arquivos Markdown.

## 1. Crie sua pasta

No GitHub, acesse a trilha desejada e entre na
pasta `materiais/`.

Clique em **Add file → Create new file**.

No nome do arquivo, digite:

`nome-do-tutorial/index.md`

Use um nome curto, sem espaços ou acentos.

## 2. Configure o card

No `index.md`, cole:

```yaml
---
title: "Nome do tutorial"
description: "Breve descrição do material."
nivel: 0
ordem: 0
destino: "conteudo.md"
---
```

- **title:** nome exibido no card.
- **description:** descrição curta.
- **nivel:** linha da árvore (0, 1, 2...).
- **ordem:** posição do card dentro do nível.
- **destino:** arquivo ou link que será aberto.

## 3. Escreva o conteúdo

Na mesma pasta, crie `conteudo.md`.

Exemplo:

```md
# Meu primeiro tutorial

## Introdução

Explique brevemente o que será ensinado.

## Passo a passo

1. Primeiro passo.
2. Segundo passo.
3. Terceiro passo.

## Resultado

Mostre o resultado final.
```

Você pode adicionar imagens, vídeos e links
para materiais complementares.

## 4. Publique

Clique em **Commit changes** para salvar os arquivos.

Após a publicação pelo GitHub Actions,
o novo tutorial aparecerá automaticamente
na árvore da trilha escolhida.

Pronto! Não é necessário editar os cards
nem modificar nenhum script.
