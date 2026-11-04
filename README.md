# LDTT HUB de Capacitação

Site: https://ldttfurb.github.io/LDTT_Capacitacao/

O HUB reúne trilhas e tutoriais do LDTT/FURB. O conteúdo é escrito em Markdown e publicado com Zensical no GitHub Pages.

## Estrutura

```text
docs/trilhas/tutoriais/
├── unity/
│   ├── index.md                 # Metadados do card da trilha
│   ├── conteudo.md              # Apresentação e <!-- GERAR_CARDS -->
│   └── materiais/
│       ├── 01-preparacao-do-ambiente/
│       │   ├── index.md         # Metadados e posição do card
│       │   └── conteudo.md      # Texto do tutorial
│       └── 03-git-clone-e-branches/
│           └── index.md         # Referência ao tutorial da trilha Git
├── git/
├── csharp/
├── boas-praticas/
└── vr/
```

Cada tutorial tem **uma única cópia** do texto em `conteudo.md`, na trilha proprietária. Outras trilhas podem mostrar um card que aponta para esse conteúdo.

## Publicar um tutorial

O autor entrega apenas um `.md`. O responsável escolhe a trilha, coloca o texto em `materiais/<tutorial>/conteudo.md` e cria um `index.md` na mesma pasta:

```yaml
---
title: "Introdução ao Git/GitHub"
description: "Obtenha o projeto e crie uma branch."
pai: null
nivel: 0
ordem: 0
destino: "conteudo.md"
---
```

`pai` é a pasta do pai dentro da mesma árvore. Use `null` e `nivel: 0` na raiz; cada filho tem nível igual à profundidade real. `ordem` ordena irmãos; empates são resolvidos pelo nome da pasta. Uma árvore com materiais deve ter uma raiz. Pais, níveis, ciclos e destinos são validados no build.

Para reutilizar o tutorial em outra trilha, crie apenas `materiais/<nome-do-card>/index.md` nela:

```yaml
---
referencia: "git/introducao-git"
pai: "01-preparacao-do-ambiente"
nivel: 1
ordem: 1
---
```

O card de referência recebe título, descrição e link do tutorial real; sua posição é independente na árvore atual. Ele não traz os filhos da trilha de origem.

Para criar uma nova trilha, adicione `docs/trilhas/tutoriais/<trilha>/index.md` com `title`, `description` e `tags`, e `conteudo.md` com exatamente um `<!-- GERAR_CARDS -->`. Não há cadastro manual no Python. Veja o guia [Enviar Tutorial](docs/trilhas/tutoriais/como-criar-tutorial/conteudo.md).

## Geração e publicação

O workflow executa `python scripts/gerar_cards.py`, `python scripts/gerar_arvores.py` e `zensical build --clean`. O primeiro gerador cria os cards das trilhas; o segundo descobre os `index.md` dos materiais, valida a hierarquia, resolve referências e insere as árvores nas páginas das trilhas. `scripts/redirecionamentos_antigos.json` preserva links publicados antes da reorganização; ele não participa da montagem das árvores.

Para testar localmente, instale `zensical` e `pyyaml`, execute os dois geradores na ordem acima e depois o build. Os arquivos gerados no diretório `docs/` são produzidos durante a publicação; não precisam entrar no commit.
