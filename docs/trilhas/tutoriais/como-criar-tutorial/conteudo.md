
# Como criar um tutorial

O HUB de Capacitação do LDTT reúne materiais de estudo desenvolvidos e indicados pelos bolsistas do laboratório.

Neste guia, você aprenderá a publicar seu próprio tutorial no GitHub.

**Você não precisa programar o HUB!** Basta criar os arquivos seguindo o modelo abaixo. Os cards são gerados automaticamente.

---

## 1. Entenda a estrutura

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

## 2. Como criar uma nova trilha

Se o assunto ainda não possui uma trilha, você pode criar uma.

### Passo 1 — Criar a pasta

No [repositório do LDTT](https://github.com/LDTTFURB/LDTT_Capacitacao), acesse:

`docs/trilhas/tutoriais/`

Clique em **Add file → Create new file**.

No campo de nome, digite:

`nome-da-trilha/index.md`

O GitHub criará o caminho ao salvar o arquivo.

Use nomes sem espaços ou acentos, por exemplo `python`, `unity` ou `desenvolvimento-web`.

### Passo 2 — Preencher o index.md

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

### Passo 3 — Criar o conteudo.md

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

## 3. Como adicionar um tutorial a uma trilha existente

Se você deseja adicionar um tutorial de Unity, por exemplo, **não precisa criar outra trilha**.

Acesse:

`docs/trilhas/tutoriais/unity/materiais/`

### Passo 1 — Criar a pasta do tutorial

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

### Passo 2 — Configurar o card

No `index.md`, utilize:

```yaml
---
title: "Meu primeiro tutorial"
description: "Aprenda a realizar uma tarefa na Unity."
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
| `nivel` | Define em qual linha da árvore o card aparece. |
| `ordem` | Define a posição entre os cards do mesmo nível. |
| `destino` | Define o arquivo ou link aberto ao clicar. |
| `ramo` | Opcional. Nome da ramificação, como Unity ou Git/GitHub. |
| `etapa` | Opcional. Ordena os blocos de ramificações; começa em `0`. |
| `ordem_ramo` | Opcional. Ordena as ramificações dentro da mesma etapa; começa em `0`. |

### Como funcionam os níveis?

Os tutoriais são apresentados em uma árvore de aprendizado.

- `nivel: 0` — primeira linha.
- `nivel: 1` — segunda linha.
- `nivel: 2` — terceira linha.

Tutoriais do mesmo nível aparecem lado a lado.

### Como funciona a ordem?

O campo `ordem` é opcional.

- `ordem: 0` — posição padrão.
- `ordem: 1`, `2`, `3`... — permitem reorganizar os cards.

Quando os valores são iguais, os cards seguem a ordem alfabética dos nomes das pastas.

### Como criar ramificações por assunto?

Use ramificações quando uma trilha reunir assuntos que podem ser consultados separadamente. No `index.md` de cada material, acrescente os campos abaixo:

```yaml
ramo: 'Unity'
etapa: 1
ordem_ramo: 0
nivel: 0
ordem: 0
```

Nesse exemplo, o tutorial aparece no primeiro nível da ramificação Unity. Para colocar outro material abaixo dele, mantenha `ramo`, `etapa` e `ordem_ramo` e use `nivel: 1`.

Na trilha de desenvolvimento com Unity, a organização é:

| Etapa | Ramificação | `ordem_ramo` |
| --- | --- | --- |
| `0` | Comece aqui | `0` |
| `1` | Unity | `0` |
| `1` | Git/GitHub | `1` |
| `1` | C\# e boas práticas | `2` |
| `2` | Prática e rotina no laboratório | `0` |

As ramificações da mesma etapa aparecem lado a lado quando houver espaço na tela. Em telas menores, ficam uma abaixo da outra. O campo `nivel` organiza os materiais dentro de cada ramificação, e `ordem` organiza materiais do mesmo nível.

Use os mesmos valores de `etapa` e `ordem_ramo` em todos os materiais de uma ramificação. Descreva no conteúdo os pré-requisitos que vêm de outro assunto e inclua links para eles. Os conectores do mapa indicam uma sequência de estudo sugerida.

Os campos novos são opcionais. Trilhas sem `ramo` continuam usando a árvore por níveis descrita acima. Se apenas parte dos materiais tiver `ramo`, os demais aparecerão em uma ramificação chamada Geral.

Para nomes com `C\#`, use aspas simples no YAML, como `ramo: 'C\# e boas práticas'`. Assim, a barra é preservada no arquivo e o card exibe o nome corretamente.

### Passo 3 — Criar o conteúdo

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

## 4. Como adicionar imagens, vídeos e links

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

## 5. Como publicar

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

## 6. Antes de finalizar

Confira:

- [ ] Criei a pasta no local correto.
- [ ] Preenchi corretamente o `index.md`.
- [ ] Criei o `conteudo.md`, se necessário.
- [ ] Verifiquei os links e imagens.
- [ ] Salvei as alterações no GitHub.

**Lembre-se:** você não precisa editar os cards do HUB nem modificar scripts. Basta criar os arquivos corretamente.

Em caso de dúvidas, consulte outros tutoriais já publicados como exemplo.
