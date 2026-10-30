# Rotina de trabalho e solução de problemas

## Objetivo

Consolide a integração e aprenda a comunicar impedimentos à equipe.

## Pré-requisitos

Concluir [Introdução geral](../unity/introducao-geral.md). Use o diagnóstico sempre que precisar de ajuda. Para encerrar a primeira entrega, conclua [Implemente e teste sua primeira alteração](../unity/primeira-alteracao.md) e [Pull Request, revisão e próxima tarefa](../git/pull-request-e-revisao.md); o PR pode estar aguardando revisão.

## Diagnóstico inicial

| Situação | Primeira verificação |
| --- | --- |
| O repositório não aparece ou não pode ser clonado. | Confira a conta usada, o convite e a permissão de acesso. |
| O Unity Hub informa que falta uma versão do Editor. | Confira `ProjectVersion.txt` e instale a versão correspondente. |
| A Unity propõe atualizar ou converter o projeto. | Interrompa a abertura e confirme a versão com o responsável. |
| O projeto apresenta erros de compilação. | Leia os erros do Console; verifique branch, versão e instruções do README. |
| Um script não abre na IDE ou os tipos Unity não são reconhecidos. | Confira o editor externo configurado e a integração da IDE com Unity. |
| O jogo abre em uma tela inesperada. | Confirme se a cena inicial correta está aberta. |
| A alteração desapareceu ao sair do Play. | Reaplique no modo de edição e salve a cena ou o asset correspondente. |
| Apareceram muitos arquivos alterados sem uma mudança intencional. | Revise as diferenças e confira versão e configurações antes de fazer commit. |
| O Pull Request está direcionado à `main`. | Corrija a branch de destino para `develop` antes de solicitar a revisão. |
| Há conflito em uma cena ou prefab. | Combine a resolução com os envolvidos antes de escolher ou descartar uma versão. |

Ao pedir ajuda, informe o que tentou fazer, o resultado esperado, o resultado obtido e os passos para reproduzir. Reproduzir é repetir as ações que fazem o problema aparecer. Inclua a mensagem de erro, a cena envolvida e a branch utilizada quando isso ajudar na análise.

Um relato pode seguir este exemplo:

> Na cena de menu, abri Opções e cliquei em Voltar. Eu esperava retornar ao menu principal, mas a tela ficou vazia. O problema ocorre sempre que repito esses passos. Não apareceu mensagem de erro no Console.

Complete o relato com o nome da sua branch e o número da versão do Editor. No seu pedido de ajuda, substitua o cenário pelos passos que você executou.

## Checklist geral da integração

### Ambiente e acesso

- [ ] Tenho acesso ao repositório correto.
- [ ] Instalei o Unity Hub e a versão do Editor exigida pelo projeto.
- [ ] Configurei a IDE e consigo abrir os scripts.
- [ ] Configurei o GitHub Desktop ou meu fluxo de Git pelo terminal.
- [ ] Li o README e executei as instruções de configuração.
- [ ] Abri a cena inicial e executei o projeto.

### Conhecimento do projeto

- [ ] Entendi o objetivo do projeto e quem pode me orientar.
- [ ] Localizei cenas, scripts, prefabs e outros recursos principais.
- [ ] Li os documentos de boas práticas e nomenclatura.
- [ ] Entendi o papel de `main`, `develop` e da minha branch.

### Primeira entrega

- [ ] Alinhei uma tarefa pequena com a equipe.
- [ ] Criei minha branch a partir da `develop` atualizada.
- [ ] Implementei e testei a alteração.
- [ ] Revisei os arquivos antes do commit.
- [ ] Fiz commits com mensagens claras e enviei a branch ao GitHub.
- [ ] Abri um PR da minha branch para `develop`, descrevendo as mudanças e a verificação.
- [ ] Aguardei a revisão e respondi aos ajustes solicitados.

**Para o dia a dia:** atualize a base antes de iniciar uma tarefa, trabalhe em uma branch própria, teste, revise seus arquivos e envie um PR claro. Compartilhe dúvidas e dificuldades com a equipe ao longo do trabalho.

## Pratique um pedido de ajuda

Escolha um impedimento encontrado durante a integração ou um exemplo discutido com seu orientador. Descreva o resultado esperado, o ocorrido, os passos para reproduzir, a versão do Editor e a branch. Inclua a mensagem de erro quando existir. Apresente esse relato ao colega que acompanha sua integração.

Se seu PR ainda estiver em revisão, mantenha esse item do checklist pendente até receber o retorno. Não faça o merge para concluir a trilha.

## Resultado e critérios de conclusão

- [ ] Sei fazer as verificações iniciais antes de pedir ajuda.
- [ ] Consigo relatar um problema com informações úteis para reproduzi-lo.
- [ ] Revisei o checklist e identifiquei eventuais pendências com a equipe.

## Navegação

[← Anterior: Introdução geral](../unity/introducao-geral.md)
