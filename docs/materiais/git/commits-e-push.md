# Registre commits e envie sua branch

## Objetivo

Revise as alterações, registre commits claros e envie o trabalho ao GitHub.

## Pré-requisitos

Concluir [Introdução ao Git/GitHub](introducao-git.md). Para executar os passos no projeto do laboratório, tenha uma alteração implementada e testada, como a de [Implemente e teste sua primeira alteração](../unity/primeira-alteracao.md). Você também pode praticar em um repositório de treinamento.

## Registre e envie suas alterações

Um commit registra um conjunto de alterações no histórico local. Sua mensagem deve explicar o que mudou de forma clara.

O guia sugere os prefixos `feat/` para implementações e `fix/` para correções:

```text
feat/ adiciona instruções ao tutorial inicial
fix/ corrige retorno do menu de pausa
fix/ impede pontuação duplicada na mesma interação
```

Evite mensagens vagas, como `alterações`, `teste` ou `arrumei`.

### Passo a passo no GitHub Desktop

1. Confira se a branch selecionada é a sua branch de trabalho.
2. Revise a lista de arquivos alterados e as diferenças apresentadas.
3. Marque na lista apenas os arquivos cujas alterações pertencem ao commit. Se houver mudanças sem relação com a tarefa no mesmo arquivo, peça ajuda para separá-las antes de continuar.
4. Escreva uma mensagem clara e acrescente uma descrição quando necessário.
5. Faça o commit.
6. Publique a branch com **Publish branch**, se for o primeiro envio, ou envie os novos commits com **Push origin**. Depois, abra o repositório no GitHub, selecione sua branch e confira se o commit aparece no histórico.

> Fazer commit registra o trabalho localmente. Fazer push envia os commits para o GitHub. Verifique se enviou o trabalho antes de encerrar sua atividade.

## Resultado e critérios de conclusão

- [ ] Revisei os arquivos e as diferenças antes do commit.
- [ ] Usei uma mensagem clara e compatível com a alteração.
- [ ] Publiquei a branch ou fiz push e confirmei que o trabalho chegou ao GitHub.

## Navegação

[← Anterior: Introdução ao Git/GitHub](introducao-git.md)

[Próximo: Pull Request, revisão e próxima tarefa →](pull-request-e-revisao.md)
