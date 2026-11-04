# Como criar e enviar um tutorial

## Para quem escreve

Entregue **um único arquivo Markdown (`.md`)** ao responsável pelo HUB. Escreva o título, as explicações, exemplos, imagens e links. Você não precisa criar pastas, configurar cards, escrever YAML ou definir a ordem da trilha.

````md
# Introdução ao Git

## Objetivo

Aprenda os fundamentos do Git.

## Instalação

Veja a [página oficial do Git](https://git-scm.com/).

```bash
git --version
```
````

## Para quem publica

1. Escolha a trilha proprietária e crie `docs/trilhas/tutoriais/<trilha>/materiais/<tutorial>/`.
2. Coloque o arquivo recebido nessa pasta com o nome `conteudo.md`. Preserve sua redação; ajuste apenas endereços de links relativos se a mudança de pasta exigir.
3. Crie um `index.md` na mesma pasta. Ele define o card e sua posição:

```yaml
---
title: "Introdução ao Git"
description: "Aprenda os fundamentos do Git."
pai: null
nivel: 0
ordem: 0
destino: "conteudo.md"
---
```

`pai` é o nome da pasta do card pai **na mesma trilha**. A raiz usa `null` e nível `0`; cada filho usa o nível do pai mais um. `ordem` define a posição entre irmãos; em empate, o nome da pasta desempata. Uma árvore com materiais deve ter uma única raiz. O gerador valida pais, níveis, ciclos e destinos durante a publicação.

Para mostrar o mesmo tutorial em outra trilha, crie ali apenas uma pasta e um `index.md` de referência. Não copie o texto:

```yaml
---
referencia: "git/introducao-git"
pai: "introducao-geral"
nivel: 1
ordem: 1
---
```

A referência usa o título, a descrição e o link do tutorial real. Seu `pai`, `nivel` e `ordem` posicionam o card nessa árvore. Ela não incorpora os filhos do tutorial de origem.

## Criar uma trilha

Crie `docs/trilhas/tutoriais/<trilha>/index.md` para o card principal:

```yaml
---
title: "Nova área"
description: "Tutoriais deste assunto."
tags:
  - Assunto
---
```

Crie também `conteudo.md` na pasta da trilha, com a apresentação e exatamente um marcador `&lt;!-- GERAR_CARDS --&gt;`. Depois adicione os materiais em `materiais/<tutorial>/`. Os geradores descobrem as trilhas e os materiais automaticamente; não é preciso editar Python.

Ao enviar a alteração para `main`, o GitHub Actions gera os cards e publica o site.
