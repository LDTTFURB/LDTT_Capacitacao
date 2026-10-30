
# Como criar um tutorial

O HUB de Capacitação do LDTT reúne materiais de estudo desenvolvidos e indicados pelos bolsistas do laboratório.

Neste guia, você aprenderá a publicar seu próprio tutorial no GitHub.

**Você não precisa programar o HUB!** Basta criar os arquivos seguindo o modelo abaixo. Os cards são gerados automaticamente.

---

## Entenda a estrutura

O HUB possui dois tipos de conteúdo:

- **Trilhas:** áreas principais, como Unity, Web e Python. Uma trilha também pode ficar dentro de outra, como VR dentro de Unity.
- **Materiais:** tutoriais individuais dentro de uma trilha.

Todos utilizam arquivos Markdown (`.md`).

Cada conteúdo possui dois arquivos:

| Arquivo | Função |
|---|---|
| `index.md` | Informações utilizadas para criar o card. |
| `conteudo.md` | Texto, imagens, vídeos e links do tutorial. |

**Importante:** o `index.md` possui apenas informações de configuração. O conteúdo que as pessoas vão ler fica no `conteudo.md`.

---

## Como criar uma nova trilha

Se o assunto ainda não possui uma trilha, você pode criar uma.

### Criar a pasta

No [repositório do LDTT](https://github.com/LDTTFURB/LDTT_Capacitacao), acesse:

`docs/trilhas/tutoriais/`

Clique em **Add file → Create new file**.

No campo de nome, digite:

`nome-da-trilha/index.md`

O GitHub criará o caminho ao salvar o arquivo.

Use nomes sem espaços ou acentos, por exemplo `python`, `unity` ou `desenvolvimento-web`.

### Preencher o index.md

Copie o exemplo:

```yaml
---
title: "Nome da trilha"
description: "Breve descrição do conteúdo."
tags:
  - Tecnologia
---
```

**O que significa cada campo?**

- `title`: nome exibido no card.
- `description`: pequena descrição do material.
- `tags`: palavras utilizadas na busca do HUB.

Você pode adicionar várias tags:

```yaml
tags:
  - Unity
  - Jogos
  - CSharp
```

Não é necessário cadastrar as tags em outro lugar.

**Para colocar a trilha dentro de outra**, informe o nome da pasta da trilha-mãe. O card aparecerá dentro dela, e a busca por tag continuará encontrando a trilha:

```yaml
pai: 'unity'
```

**Para indicar outras trilhas no fim da página**, liste o nome das pastas. O título e a descrição são copiados de cada trilha:

```yaml
relacionadas:
  - 'git'
  - 'boas-praticas'
```

### Criar o conteudo.md

Na mesma pasta, crie `conteudo.md`.

Exemplo:

```md
# Nome da trilha

Breve apresentação do conteúdo.

## Introdução

Explique o assunto.

## Materiais

Adicione textos, vídeos e links.
```

**Pronto!** Após a publicação, o HUB criará automaticamente um card para essa trilha e, quando ela tiver materiais, a árvore de conteúdos.

---

## Como adicionar um tutorial a uma trilha existente

Se você deseja adicionar um tutorial de VR, por exemplo, **não precisa criar outra trilha**.

Acesse:

`docs/trilhas/tutoriais/vr/materiais/`

### Criar a pasta do tutorial

Clique em **Add file → Create new file**.

Digite:

`meu-tutorial/index.md`

A estrutura ficará assim:

```text
vr/
└── materiais/
    └── meu-tutorial/
        ├── index.md
        └── conteudo.md
```

### Configurar o card

No `index.md`, utilize:

```yaml
---
title: "Meu primeiro tutorial"
description: "Aprenda a realizar uma tarefa na Unity."
pai: "01-introducao-a-vr"
---
```

**Explicação dos campos:**

| Campo | Função |
|---|---|
| `title` | Nome do card. |
| `description` | Descrição curta. |
| `pai` | Nome exato da pasta do conteúdo pai. Somente a raiz da árvore não tem pai. |
| `ordem` | Opcional. Define a posição entre conteúdos com o mesmo pai. Sem ele, vale a ordem alfabética das pastas. |
| `destino` | Opcional. Define o arquivo ou link aberto ao clicar. Sem ele, abre o `conteudo.md`. |

### Como montar uma árvore de conteúdos?

Cada material informa seu pai no `index.md`. Por exemplo, a árvore de VR é formada assim:

```yaml
# 01-introducao-a-vr: a raiz, sem pai
title: 'Introdução à VR'

# 04-quest-preparacao: filho da raiz
title: 'Prepare o headset e o projeto para o Meta Quest'
pai: '01-introducao-a-vr'

# 05-quest-primeira-cena: neto da raiz
title: 'Crie sua primeira cena interativa no Quest'
pai: '04-quest-preparacao'
```

Os exemplos mostram os campos de hierarquia. Cada `index.md` também precisa de `description`.

O resultado é uma árvore com relações explícitas:

```text
Introdução à VR
├── Prepare o projeto para o Google Cardboard
│   └── Execute a cena de exemplo no celular
└── Prepare o headset e o projeto para o Meta Quest
    └── Crie sua primeira cena interativa no Quest
```

- A árvore possui uma única raiz, sem `pai`.
- O pai precisa existir na mesma pasta `materiais`. Um conteúdo não pode ser pai de si mesmo nem formar um ciclo com outros materiais.
- Use títulos sem numeração. A posição na árvore é definida pelos metadados.
- Não escreva links de "Anterior" e "Próximo": a seção **Navegação** é criada a partir da árvore.

As linhas da árvore indicam parentesco por assunto. Explique no texto os pré-requisitos de estudo ou de prática, incluindo links para outras trilhas quando necessário. Em telas menores, a árvore fica vertical e mantém a indentação dos filhos.

Para títulos com `C#`, use aspas simples no YAML, como `title: 'Introdução ao C#'`.

### Criar o conteúdo

Na mesma pasta, crie `conteudo.md`.

Exemplo:

```md
# Meu primeiro tutorial

## Objetivo

Explique o que será aprendido.

## Passo a passo

1. Abra a ferramenta.
2. Configure o ambiente.
3. Execute o exemplo.

## Resultado

Mostre o resultado obtido.

## Referências

Adicione os materiais consultados.
```

Você pode adaptar as seções conforme a necessidade do tutorial.

---

## Como adicionar imagens, vídeos e links

O Markdown permite incluir diferentes tipos de conteúdo.

**Link para outro site:**

```md
[Documentação da Unity](https://docs.unity3d.com/)
```

**Imagem:**

Crie uma pasta `imagens/` ao lado do `conteudo.md` e adicione:

```md
![Descrição da imagem](imagens/exemplo.png)
```

**Vídeo:**

Você pode adicionar um link para o vídeo:

```md
[Assistir ao vídeo](https://www.youtube.com/)
```

Se o tutorial for apenas um link externo, você também pode informar o endereço diretamente no campo `destino` do `index.md` de um material:

```yaml
destino: "https://exemplo.com/tutorial"
```

Nesse caso, o card abrirá o endereço externo e não será necessário criar um `conteudo.md` para esse material.

---

## Como publicar

Depois de criar os arquivos:

1. Confira se o `index.md` possui todos os campos necessários.
2. Verifique se os links e imagens estão corretos.
3. Clique em **Commit changes** para salvar em uma branch.
4. Envie um **Pull Request**. O GitHub confere os metadados, os links e a geração do site, e aponta o que precisa ser corrigido.
5. Confira o resultado da verificação e faça o merge.
6. Após a alteração entrar na branch `main`, o GitHub Actions atualizará o HUB automaticamente.

Se a verificação encontrar um erro em um commit feito direto na `main`, o site anterior continua no ar até a correção.

Você pode acompanhar a publicação na aba [Actions](https://github.com/LDTTFURB/LDTT_Capacitacao/actions).

Quando a publicação for concluída, acesse o [HUB de Trilhas](https://ldttfurb.github.io/LDTT_Capacitacao/trilhas/).

Seu novo conteúdo deverá aparecer automaticamente!

---

## Antes de finalizar

Confira:

- [ ] Criei a pasta no local correto.
- [ ] Preenchi corretamente o `index.md`.
- [ ] Criei o `conteudo.md`, se necessário.
- [ ] Verifiquei os links e imagens.
- [ ] Salvei as alterações no GitHub.

**Lembre-se:** você não precisa editar os cards do HUB nem modificar scripts. Basta criar os arquivos corretamente.

Em caso de dúvidas, consulte outros tutoriais já publicados como exemplo.
