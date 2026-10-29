
# Como criar um tutorial

O HUB de Capacitação do LDTT reúne materiais de estudo desenvolvidos e indicados pelos bolsistas do laboratório.

Neste guia, você aprenderá a publicar seu próprio tutorial no GitHub.

**Você não precisa programar o HUB!** Basta criar os arquivos seguindo o modelo abaixo. Os cards são gerados automaticamente.

---

## Entenda a estrutura

O HUB possui dois tipos de conteúdo:

- **Trilhas:** áreas principais, como Unity, Web e Python.
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

**Pronto!** Após a publicação, o HUB criará automaticamente um card para essa trilha.

---

## Como adicionar um tutorial a uma trilha existente

Se você deseja adicionar um tutorial de Unity, por exemplo, **não precisa criar outra trilha**.

Acesse:

`docs/trilhas/tutoriais/unity/materiais/`

### Criar a pasta do tutorial

Clique em **Add file → Create new file**.

Digite:

`meu-tutorial/index.md`

A estrutura ficará assim:

```text
unity/
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
pai: null
nivel: 0
ordem: 0
destino: "conteudo.md"
---
```

**Explicação dos campos:**

| Campo | Função |
|---|---|
| `title` | Nome do card. |
| `description` | Descrição curta. |
| `nivel` | Profundidade do conteúdo: raiz em `0`, filhos em `1`, netos em `2` e assim por diante. |
| `ordem` | Define a posição entre conteúdos com o mesmo pai. |
| `destino` | Define o arquivo ou link aberto ao clicar. |
| `pai` | Nome exato da pasta do conteúdo pai; use `null` na raiz. |

### Como montar uma árvore de conteúdos?

Cada material informa seu pai no `index.md`. A introdução geral é a raiz da árvore e utiliza:

```yaml
title: 'Introdução geral'
pai: null
nivel: 0
ordem: 0
```

Para ligar a introdução à Unity à introdução geral, use o nome da pasta da introdução geral:

```yaml
title: 'Introdução à Unity'
pai: '01-preparacao-do-ambiente'
nivel: 1
ordem: 0
```

Para colocar áudio como filho da introdução à Unity:

```yaml
title: 'Áudio: organização e reprodução'
pai: '04-primeira-execucao-na-unity'
nivel: 2
ordem: 1
```

Os exemplos mostram os campos de hierarquia. Cada `index.md` também precisa de `description` e `destino`, apresentados no modelo acima.

O resultado é uma árvore com relações explícitas:

```text
Introdução geral
├── Introdução à Unity
│   ├── Interface
│   └── Áudio
├── Introdução ao Git/GitHub
└── Introdução ao C#
```

- A árvore possui uma única raiz, com `pai: null` e `nivel: 0`.
- Cada filho informa o nome da pasta do pai e usa um nível a mais que ele.
- `ordem` organiza os filhos de um mesmo pai. Em caso de empate, vale a ordem alfabética das pastas.
- O pai precisa existir na mesma pasta `materiais`. Um conteúdo não pode ser pai de si mesmo nem formar um ciclo com outros materiais.
- Use títulos sem numeração. A posição na árvore é definida pelos metadados.

As linhas da árvore indicam parentesco por assunto. Explique no texto os pré-requisitos de estudo ou de prática, incluindo links para outros ramos quando necessário. Em telas menores, a árvore fica vertical e mantém a indentação dos filhos.

Preencha `pai` em todos os materiais da trilha ao adotar esse modelo. Trilhas sem esse campo continuam usando a apresentação antiga, por níveis. Os campos `ramo`, `etapa` e `ordem_ramo` não são usados na árvore de pais e filhos.

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
3. Clique em **Commit changes** para salvar.
4. Caso esteja trabalhando em uma branch, envie um **Pull Request** para revisão.
5. Após a alteração entrar na branch `main`, o GitHub Actions atualizará o HUB automaticamente.

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
