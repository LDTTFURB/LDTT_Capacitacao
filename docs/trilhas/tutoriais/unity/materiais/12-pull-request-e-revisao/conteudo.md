# Pull Request, revisão e próxima tarefa

## Objetivo

Solicite a revisão da entrega e acompanhe sua integração em develop.

## Pré-requisitos

Concluir [Registre commits e envie sua branch](../11-commits-e-push/conteudo.md) e confirmar que os commits da sua tarefa chegaram ao GitHub. Para a primeira entrega no laboratório, utilize a alteração testada em [Implemente e teste sua primeira alteração](../10-primeira-alteracao/conteudo.md).

## Apresente sua entrega

Um **Pull Request (PR)** é um pedido de revisão das alterações de uma branch. Depois da aprovação, o **merge** integra essas alterações à branch de destino.

O fluxo definido pelo LDTT é:

```text
SUA BRANCH → develop → main
```

### Abra um pedido de integração na develop

1. Após o push, abra um Pull Request pelo GitHub Desktop ou pelo GitHub.
2. Confira a branch de destino (**base**): deve ser `develop`.
3. Confira a branch de origem (**compare**): deve ser sua branch de trabalho.
4. Escreva um título que represente a tarefa.
5. Resuma as principais mudanças e explique como foram verificadas.
6. Envie para revisão conforme o procedimento da equipe.

Modelo de descrição sugerido:

```markdown
## Objetivo
Descreva o problema ou a funcionalidade atendida.

## Alterações
- Primeira mudança relevante.
- Segunda mudança relevante, se houver.

## Como foi verificado
1. Cena ou fluxo utilizado.
2. Ações realizadas.
3. Resultado observado.

## Pendências
Informe limitações ou pontos que precisam de acompanhamento, se houver.
```

### Aguarde a revisão

Conforme o guia, **aguarde um dos responsáveis analisar e aceitar o merge**. Não faça a integração por conta própria.

Se houver pedidos de ajuste, faça as correções na mesma branch, teste novamente, crie novos commits e faça push. Eles serão incluídos no PR existente.

Caso apareça um conflito, peça orientação antes de descartar alterações. Esse cuidado é especialmente útil em cenas e prefabs, cujos arquivos podem ser difíceis de comparar manualmente.

### Comece a próxima tarefa

Após o merge:

1. Volte para a `develop`.
2. Atualize sua cópia local.
3. Crie uma nova branch para a próxima tarefa.

Para a próxima tarefa, siga esse fluxo de nova branch: ele ajuda a separar o histórico das entregas. Se a equipe propuser outra operação de Git, peça que explique quando e como aplicá-la.

A integração de `develop` em `main` segue o fluxo de estabilização e revisão conduzido pelos responsáveis do projeto.

## Resultado e critérios de conclusão

- [ ] Abri o PR da minha branch para develop.
- [ ] Descrevi as mudanças e como foram verificadas.
- [ ] Respondi aos ajustes pedidos ou registrei que estou aguardando revisão.
- [ ] Após o merge, sei atualizar develop e iniciar a próxima tarefa em uma nova branch.

## Navegação

[← Voltar à árvore de conteúdos](../../conteudo.md)

**Conteúdo pai:** [Registre commits e envie sua branch](../11-commits-e-push/conteudo.md).

**Conteúdos relacionados:**

- [Rotina de trabalho e solução de problemas](../13-rotina-e-solucao-de-problemas/conteudo.md).
