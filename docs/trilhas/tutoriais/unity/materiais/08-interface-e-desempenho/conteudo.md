# 08. Interface: resolução, painéis e desempenho

## Objetivo

Verifique se a interface funciona nas telas previstas, acompanhe a abertura de painéis e entenda os conceitos básicos de desempenho visual.

## Pré-requisitos

Concluir o tutorial 07: Padrões de projeto na Unity.

## 1. Configuração da interface

A interface precisa continuar legível e utilizável nas telas previstas para o jogo. **Resolução** é a quantidade de pixels da imagem, como 1920 × 1080. **Proporção** é a relação entre largura e altura, como 16:9. Ao mudar de tela, um botão pode ficar cortado ou cobrir outro elemento; por isso, teste as opções indicadas pela equipe.

1. Pergunte quais dispositivos e resoluções o projeto atende.
2. Localize uma tela de interface e descubra como ela foi organizada no projeto.
3. Execute essa tela nas proporções previstas pela equipe.
4. Observe legibilidade, cortes, sobreposição de elementos e acesso aos botões.
5. Registre um problema reproduzível, se houver, antes de alterar a configuração.

**Estudo indicado:** [Configuração de interface — EN](https://youtu.be/VHFJgQraVUs) e [PT-BR](https://youtu.be/5rosjAX2Cag).

## 2. Draw calls e batches

Uma **draw call** é uma solicitação de desenho enviada à placa gráfica. Um **batch** reúne elementos que podem ser processados juntos. **Renderização** é o processo de gerar a imagem exibida na tela. Estude como as escolhas da interface afetam esse trabalho. Compartilhar recursos pode favorecer o agrupamento, mas o resultado depende do projeto e precisa ser medido.

Antes de propor uma otimização, combine com a equipe o cenário e a ferramenta de medição. Compare o mesmo cenário antes e depois, preservando a aparência e o comportamento da interface.

**Estudo indicado:** [Draw calls — EN](https://youtu.be/_EmwV98r4RY) e [PT-BR](https://youtu.be/tfqwa-eImcw). Ao estudar, anote quais escolhas de organização da interface podem afetar o desenho dos elementos.

## 3. Gerenciamento de painéis

Um painel agrupa elementos de uma tela, como os controles do menu de pausa. Um pop-up é uma janela que aparece sobre a tela atual, como uma confirmação de saída. Um gerenciador de painéis organiza quando cada um deve abrir e fechar. Antes de criar outro gerenciador, procure a solução já adotada pelo projeto.

1. Identifique quem abre e fecha os painéis.
2. Acompanhe a abertura de uma tela e o retorno à tela anterior.
3. Verifique o que deve acontecer quando um pop-up é fechado.
4. Confira os nomes de scripts e prefabs de interface com o prefixo `UI`.

**Estudo indicado:** [Panel Manager — EN](https://youtu.be/texonivDsy0).

## 4. Exercício

Escolha uma tela existente, teste duas proporções de tela previstas pelo projeto e percorra um fluxo de abrir, fechar e retornar. Registre a cena, as proporções testadas e o que aconteceu. Por exemplo: “Na proporção prevista para o celular, todos os botões ficaram visíveis; ao fechar a confirmação, voltei ao menu de pausa”. Se a tarefa envolver desempenho, registre também uma comparação combinada com a equipe. Não é preciso implementar uma nova interface para concluir esta etapa.

## Resultado e critérios de conclusão

- [ ] Identifiquei as resoluções previstas para a interface.
- [ ] Percorri um fluxo de abertura e fechamento de painéis.
- [ ] Registrei a verificação e entendi a necessidade de medir antes de otimizar.

## Navegação

[← Anterior: Padrões de projeto na Unity](../07-padroes-de-projeto/conteudo.md)

[Próximo: Áudio: organização e reprodução →](../09-audio/conteudo.md)
