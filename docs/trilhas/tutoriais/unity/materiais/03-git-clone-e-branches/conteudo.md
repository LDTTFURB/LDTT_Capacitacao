# 03. Git: clone e branch de trabalho

## Objetivo

Obtenha o projeto e crie uma branch conforme o padrão do LDTT.

## Pré-requisitos

Concluir o tutorial 02: Fundamentos de C#, Unity e materiais de estudo.

## Clone o repositório

Clonar cria uma cópia local do repositório, incluindo seu histórico de alterações.

1. No GitHub Desktop, utilize a opção de clonar um repositório.
2. Selecione o repositório indicado pelo responsável.
3. Escolha uma pasta local para armazenar o projeto.
4. Aguarde a conclusão do clone.
5. Leia o README e siga eventuais instruções adicionais de configuração.

## Entenda o fluxo de branches

Uma branch é uma linha de trabalho no histórico do Git. Ela permite preparar alterações para revisão antes de integrá-las à linha compartilhada pela equipe. O fluxo do laboratório utiliza duas branches principais:

| Branch | Finalidade |
| --- | --- |
| `main` | Manter a última versão estável do projeto. |
| `develop` | Integrar o trabalho em desenvolvimento, mantendo o projeto em condições de funcionamento. |

Para implementar uma funcionalidade ou corrigir um problema, crie uma **branch própria com base na `develop`**.

### Nomeie sua branch

O padrão apresentado no guia é:

```text
descricao-da-tarefa/seu-nome
```

Exemplos ilustrativos:

```text
tutorial-inicial/bernardo
correcao-menu/ana
ajuste-pontuacao/pedro
```

Escolha um nome curto e relacionado ao trabalho. Uma nova tarefa deve, preferencialmente, começar em uma nova branch.

### Crie pelo GitHub Desktop

1. No seletor de branch do GitHub Desktop, escolha `develop`. Use **Fetch origin** para consultar novidades no GitHub e, se aparecer a opção **Pull origin**, use-a para trazer as atualizações para seu computador.
2. Crie uma nova branch a partir dela.
3. Informe o nome seguindo o padrão do laboratório.
4. Confirme que a nova branch está selecionada antes de editar os arquivos.

> Para esta integração, você pode usar um nome como `integracao-inicial/seu-nome`. Alinhe a primeira tarefa com a equipe; se ela exigir outra branch, crie-a a partir da `develop` atualizada antes de editar.

## Resultado e critérios de conclusão

- [ ] Clonei o repositório e li o README.
- [ ] Entendi o papel de main e develop.
- [ ] Criei e selecionei uma branch própria a partir da develop atualizada.

## Navegação

[← Anterior: Fundamentos de C#, Unity e materiais de estudo](../02-fundamentos-e-estudos/conteudo.md)

[Próximo: Primeira execução e exploração do projeto →](../04-primeira-execucao-na-unity/conteudo.md)
