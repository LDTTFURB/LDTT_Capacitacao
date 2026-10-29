# 06. C#: contratos, eventos e refatoração

## Objetivo

Estude interfaces, delegates, eventos, ScriptableObjects, refatoração e SOLID.

## Pré-requisitos

Concluir o tutorial 05: Nomenclatura e organização de arquivos.

## 1. Interfaces

Uma interface descreve um **contrato**: um conjunto de operações que uma classe se compromete a oferecer. Por exemplo, uma interface `ICollectable` pode definir a operação de coletar um item. Uma moeda e uma poção podem cumprir esse contrato de maneiras diferentes. Assim, o código que solicita a coleta pode trabalhar com `ICollectable`, sem precisar conhecer todos os tipos de item. Ao estudar o projeto, procure um tipo com prefixo `I` e uma classe que o implemente.

**Estudo indicado:** [Interfaces — EN](https://youtu.be/MZOrGXk4XFI).

## 2. Delegates e eventos

Um **delegate** é um tipo que permite guardar uma referência a um método compatível com uma assinatura, isto é, com os mesmos tipos de parâmetros e de retorno. Os parâmetros são os dados recebidos pelo método; o retorno é o resultado que ele devolve. `AttackDelegate` é um exemplo de nome de delegate no padrão do laboratório.

Um **evento** permite que um objeto avise outros quando algo acontece. Por exemplo, ao receber um golpe, um personagem pode emitir `OnHit`; um método chamado `Character_OnHit` pode responder atualizando a tela. Quem emite o aviso é o publicador; quem se inscreve para recebê-lo é o assinante.

No código de eventos C#, procure o uso de `+=`, que inscreve um método, e de `-=`, que remove essa inscrição. Aqui, inscrição em um evento é diferente de assinatura de método. Verifique quando o objeto começa e deixa de receber avisos. Antes de mudar esses momentos, discuta com a equipe quando os objetos são criados, ativados, desativados e destruídos.

**Estudo indicado:** [Delegates — EN](https://youtu.be/3ZfwqWl-YI0) e [Events — EN](https://youtu.be/OuZrhykVytg).

## 3. ScriptableObjects

Um **ScriptableObject** permite guardar dados em um asset da Unity, separado dos objetos da cena. Por exemplo, um asset pode reunir nome, imagem e valor de um item para consulta por outros objetos. Estude como o projeto organiza esses dados reutilizáveis. Localize um exemplo, se houver, e identifique quais dados ele armazena e quais objetos o consultam. Confira com a equipe a convenção de nome apresentada no tutorial anterior.

**Estudo indicado:** [ScriptableObjects — EN](https://youtu.be/aPXvoWVabPY) e [ScriptableObjects — PT-BR](https://youtu.be/_6yYIf__m7s).

## 4. Refatoração

Refatorar é melhorar a estrutura do código preservando seu comportamento esperado. Antes de uma mudança, registre o comportamento atual; depois, execute novamente os mesmos passos de verificação. Prefira alterações pequenas e separe refatorações amplas das tarefas de funcionalidade.

**Estudo indicado:** [Refatoração — EN](https://youtu.be/7oZBfpI_hxI) e [Refatoração — PT-BR](https://youtu.be/B2ikFkFWSLM).

## 5. Princípios SOLID

SOLID reúne cinco princípios para orientar a organização do código e facilitar mudanças. Use as perguntas abaixo para analisar um script. Neste contexto, consumidor é o código que usa outro tipo, e dependência é um recurso ou serviço de que ele precisa para funcionar.

| Princípio | Pergunta para revisar o código |
| --- | --- |
| Responsabilidade única | Esta classe reúne responsabilidades sem relação entre si? |
| Aberto/fechado | Consigo estender um comportamento sem alterar repetidamente código já utilizado? |
| Substituição de Liskov | Uma implementação pode substituir o tipo esperado sem quebrar seu contrato? |
| Segregação de interfaces | Uma classe precisa depender de uma interface com operações que ela não utiliza? |
| Inversão de dependência | O código pode depender de um contrato, como uma interface, em vez de ficar preso a uma implementação específica? |

Uma abstração representa o que vários casos têm em comum, como o contrato de coleta do primeiro exemplo. Não crie novas abstrações apenas para usar um princípio. Discuta o custo e o benefício na tarefa concreta.

**Estudo indicado:**

- [Artigo sobre SOLID — PT-BR](https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530).
- [SOLID — EN, parte 1](https://youtu.be/QDldZWvNK_E) e [parte 2](https://youtu.be/Fs8jy7DHDyc).
- [SOLID — PT-BR](https://youtu.be/6SfrO3D4dHM).

## 6. Exercício

Selecione com um colega um script pequeno e identifique sua responsabilidade e suas dependências. Procure uma interface, um evento ou um ScriptableObject relacionado, se existir. Proponha uma melhoria pequena e explique como verificaria que o comportamento foi preservado. Se o projeto não tiver esses recursos, use um exemplo do material de estudo; não introduza uma arquitetura nova apenas para completar a atividade.

## Resultado e critérios de conclusão

- [ ] Identifiquei a finalidade dos recursos apresentados.
- [ ] Analisei um exemplo do projeto ou do material de estudo.
- [ ] Propus uma melhoria e uma forma de verificar o comportamento.

## Navegação

[← Anterior: Nomenclatura e organização de arquivos](../05-nomenclatura-e-arquivos/conteudo.md)

[Próximo: Padrões de projeto na Unity →](../07-padroes-de-projeto/conteudo.md)
