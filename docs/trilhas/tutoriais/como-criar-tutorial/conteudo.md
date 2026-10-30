# Como criar e enviar um tutorial

O bolsista **só precisa escrever um arquivo Markdown (`.md`)**. Não é necessário conhecer a estrutura do GitHub, configurar cards ou criar links entre tutoriais. A organização da árvore é responsabilidade de quem publica os materiais.

## 1. Para quem vai escrever o tutorial

Crie um arquivo com um nome simples, por exemplo `introducao-git.md`, usando qualquer editor de texto que salve arquivos `.md`.

````md
# Introdução ao Git

## Objetivo

Aprenda os fundamentos do Git e os comandos mais utilizados.

## Instalação

Veja a [página oficial do Git](https://git-scm.com/).

## Comandos básicos

```bash
# Verifica a versão instalada
git --version
```
````

**Atenção:** o exemplo acima mostra um tutorial com títulos, links e um bloco de comandos. Você pode organizar o conteúdo em outras seções se fizer mais sentido.

- O primeiro `#` vira o **título do card**.
- O primeiro parágrafo de `## Objetivo` vira a **descrição do card**. Se não houver essa seção, o sistema usa o primeiro parágrafo disponível.
- Links para sites funcionam normalmente: `[Nome](https://site.com/)`.
- Envie o **arquivo `.md` pronto** ao responsável pela publicação. **Você não precisa abrir o GitHub.**

Não inclua `index.md`, `nivel`, `ordem`, `pai`, `destino` nem outros metadados apenas para gerar o card.

## 2. Para quem recebe e publica os arquivos

No repositório, coloque o arquivo recebido na pasta do assunto:

```text
docs/
└── materiais/
    ├── unity/
    │   └── introducao-unity.md
    ├── git/
    │   └── introducao-git.md
    ├── csharp/
    │   └── introducao-csharp.md
    ├── boas-praticas/
    │   └── nomenclatura-e-arquivos.md
    └── vr/
        └── introducao-vr.md
```

A pasta identifica a área e o nome do arquivo identifica o tutorial. Use nomes em minúsculas, com hífens, sem espaços ou acentos. Se possível, escolha um nome que explique o assunto, como `instalacao-do-editor.md`.

**Só colocar o arquivo na pasta já é suficiente para o sistema encontrá-lo.** Se ele ainda não fizer parte do roteiro da área, aparecerá automaticamente como **Novo tutorial** naquela trilha. O responsável pode adicioná-lo à árvore depois.

## 3. Como colocar o tutorial na árvore

Abra o arquivo da trilha na pasta `roteiros/`. Por exemplo, `roteiros/unity.md`.

```md
# Unity

- unity/introducao-geral
  - unity/introducao-unity
    - unity/audio
  - git/introducao-git
  - csharp/introducao-csharp
```

Cada linha com `-` é um card. Escreva somente a **pasta + barra + nome do arquivo sem `.md`**.

- Um item sem recuo começa um ramo.
- Dois espaços antes do `-` ligam o tutorial ao card acima.
- Quatro espaços criam um nível mais profundo; e assim por diante.
- A **ordem das linhas** é a ordem dos cards. Não é preciso preencher números.
- O arquivo pode ser reutilizado em diferentes roteiros: `git/introducao-git` pode aparecer tanto em `roteiros/git.md` quanto em `roteiros/unity.md`.

**Não é preciso escrever links.** O gerador encontra o arquivo real, extrai o título e o objetivo e cria o endereço correto do card. Se um nome estiver incorreto ou faltar um arquivo, a publicação mostrará um erro informando a linha do roteiro.

Os arquivos `roteiros/*.md` **não são tutoriais**; servem somente para organizar a apresentação dos cards.

## 4. E se eu quiser criar uma nova área?

Esta parte é feita uma única vez pelo responsável pelo HUB. Crie uma pasta em `docs/materiais/nova-area/` e uma trilha correspondente em `docs/trilhas/tutoriais/nova-area/` com:

**`index.md`**, para exibir o card na página de trilhas:

```yaml
---
title: "Nova área"
description: "Tutoriais deste assunto."
tags:
  - Assunto
---
```

**`conteudo.md`**, com a apresentação da trilha e o marcador de geração:

```md
# Nova área

Escolha um tutorial na árvore abaixo.

<!-- GERAR_CARDS -->
```

Por último, crie `roteiros/nova-area.md` com o título `# Nova área`. Já será possível incluir arquivos `.md` em `docs/materiais/nova-area/`; se não estiverem listados no roteiro, aparecerão na seção **Novos tutoriais**.

## 5. Publicação

O responsável faz o commit ou envia um Pull Request. Quando a alteração chega à branch `main`, o GitHub Actions gera os cards e publica o HUB automaticamente.

Consulte o [repositório](https://github.com/LDTTFURB/LDTT_Capacitacao) ou acompanhe o processo na [aba Actions](https://github.com/LDTTFURB/LDTT_Capacitacao/actions).

**Resumo:** quem escreve entrega **um `.md`**; quem publica coloca na pasta certa e, quando desejar, adiciona **uma linha ao roteiro**. Nenhum dos dois precisa editar o script gerador.
