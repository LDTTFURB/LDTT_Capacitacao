# 07. Padrões de projeto na Unity

## Objetivo

Reconheça Singleton, Observer, Command, State e Flyweight e avalie quando usá-los.

## Pré-requisitos

Concluir o tutorial 06: C\#: contratos, eventos e refatoração.

## 1. Entenda a finalidade antes de aplicar

Um padrão de projeto descreve uma forma conhecida de resolver um problema recorrente de organização do código. Sua escolha depende da necessidade e da arquitetura do projeto, ou seja, de como seus sistemas estão organizados e se relacionam. Na Unity, a solução também pode aproveitar recursos do motor de jogo e diferir de um exemplo escrito apenas em C\#.

Se estiver trabalhando no Furbot, siga a orientação do laboratório de priorizar os vídeos em inglês. Use os materiais em português como apoio quando precisar esclarecer um conceito.

## 2. Conheça os cinco padrões

| Padrão | Ideia principal | Situação para discutir com a equipe |
| --- | --- | --- |
| Singleton | Mantém uma única instância de uma classe e oferece um ponto de acesso a ela. | Existe um serviço que precisa dessa característica ou apenas uma conveniência de acesso? |
| Observer | Um objeto avisa outros sobre mudanças; os interessados se inscrevem e podem cancelar a inscrição. | Uma mudança de estado precisa atualizar sistemas independentes, como a vida do personagem e o indicador de vida na tela (HUD)? |
| Command | Representa uma solicitação, como mover ou atacar, em um objeto que pode ser executado depois. | É necessário armazenar, adiar ou manter histórico de ações? |
| State | Organiza em estados separados os comportamentos de um objeto, como andar e atacar. | O comportamento muda entre estados como parado, andando e atacando? |
| Flyweight | Compartilha partes do estado entre vários objetos para reduzir memória. | Muitos objetos repetem dados que poderiam ser compartilhados? |

Os cenários ajudam a reconhecer problemas que os padrões podem resolver; você não precisa implementar todos eles. No Flyweight, vários objetos compartilham dados comuns: por exemplo, árvores podem usar os mesmos dados de aparência e manter posições próprias. Já o **object pooling** reutiliza objetos criados anteriormente, como projéteis que voltam a ser usados. Essa diferença ajuda a escolher a solução adequada.

## 3. Materiais de estudo

Nas indicações, **EN** significa inglês e **PT-BR**, português brasileiro. As observações sobre legendas seguem o guia de referência do laboratório.

| Padrão | Material em inglês | Material em português |
| --- | --- | --- |
| Singleton | [EN](https://youtu.be/mpM0C6quQjs) | [PT-BR](https://www.youtube.com/watch?v=LS7CG-tryWM) |
| Observer | [EN](https://youtu.be/Yy7Dt2usGy0) | [PT-BR](https://youtu.be/EydZk5MFB78) |
| Command | [EN](https://youtu.be/UoNumkMTx-U) | [Com legenda, conforme o guia](https://youtu.be/dt-qYkZ3Mt0) |
| State | [EN, trecho indicado](https://youtu.be/hQE8lQk9ikE?t=1276) | [PT-BR](https://youtu.be/i-VkhmDfrok) |
| Flyweight | [EN, trecho indicado](https://youtu.be/hQE8lQk9ikE?t=1061) | [Com legenda, conforme o guia](https://youtu.be/By579DX9aYc) |

## 4. Exercício de análise

1. Escolha um dos padrões e estude seu material indicado.
2. Descreva o problema que ele resolve e um possível uso no projeto.
3. Procure uma implementação existente com o colega responsável.
4. Explique por que o padrão seria adequado ou desnecessário para a situação.

Para concluir a etapa, basta demonstrar essa análise. A implementação de um padrão deve fazer parte de uma tarefa acordada com a equipe.

## Resultado e critérios de conclusão

- [ ] Consigo explicar o objetivo dos cinco padrões apresentados.
- [ ] Estudei um deles e analisei um uso possível com a equipe.
- [ ] Entendi que a escolha depende da necessidade e da arquitetura do projeto.

## Navegação

[← Anterior: C\#: contratos, eventos e refatoração](../06-csharp-e-refatoracao/conteudo.md)

[Próximo: Interface: resolução, painéis e desempenho →](../08-interface-e-desempenho/conteudo.md)
