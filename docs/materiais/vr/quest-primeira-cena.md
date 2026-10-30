# Crie sua primeira cena interativa no Quest

## Objetivo

Monte uma cena com Building Blocks, execute-a no headset e meça o desempenho.

## Pré-requisitos

Concluir [Prepare o headset e o projeto para o Meta Quest](quest-preparacao.md). Mantenha o headset conectado ao computador por USB.

## O que são Building Blocks

Building Blocks são recursos prontos do Meta XR SDK que você adiciona à cena sem precisar programar. Ao adicionar um bloco, os blocos dos quais ele depende são instalados automaticamente. No laboratório, esta é a forma mais usada de montar as cenas.

Abra a janela em **Window > Meta > Meta XR SDK > Building Blocks**. Clique na imagem de um bloco para ler a descrição e em **Add Block** para adicioná-lo à cena.

| Bloco | Para que serve |
| --- | --- |
| Camera Rig | Câmera e rastreamento da cabeça; é a base da cena em VR. |
| Interactions Rig | Conjunto pronto de interações para mãos e controles. |
| Grab Interaction | Pegar e soltar um objeto próximo com as mãos ou os controles. |
| Distance Grab | Pegar um objeto a distância. |
| Ray Interaction | Apontar e selecionar com um raio. |
| Poke Interaction | Tocar em um objeto com o dedo, como em um botão. |
| Teleport | Mover-se pela cena por teletransporte. |

## Monte a cena

1. Crie uma cena nova e apague a **Main Camera**, pois o bloco **Camera Rig** adiciona a sua própria câmera.
2. Adicione um plano como chão, na posição `(0, 0, 0)`.
3. Adicione um cubo com escala `(0.1, 0.1, 0.1)` na posição `(0, 1, 0.4)`, ao alcance da pessoa.
4. Selecione o cubo na **Hierarchy**. O bloco é aplicado ao objeto selecionado; sem seleção, ele cria um cubo novo.
5. Na janela **Building Blocks**, adicione **Grab Interaction**. Os blocos **Interactions Rig** e **Camera Rig** são adicionados automaticamente.
6. Confirme que os dois blocos apareceram na **Hierarchy**.
7. Para usar as mãos, selecione o objeto que contém o componente **OVR Manager** e, em **Quest Features > General**, defina **Hand Tracking Support** como **Controllers And Hands** ou **Hands Only**.

O cubo fica sem gravidade por padrão, então permanece no ar ao ser solto. Para que ele caia, ajuste o **Rigidbody** no Inspector.

## Execute no headset

1. Abra **File > Build Profiles** e selecione **Meta Quest**. Se essa plataforma não aparecer na sua versão da Unity, selecione **Android**.
2. Clique em **Switch Platform**, se necessário.
3. Em **Open Scene List**, adicione a cena.
4. Em **Run Device**, selecione o headset. Ele aparece apenas quando está conectado por USB.
5. Ative **Development Build** durante os testes e desative-o na versão final, pois essa opção pode afetar o desempenho.
6. Clique em **Build and Run** e escolha onde salvar o `.apk`.
7. No headset, aproxime a mão ou o controle do cubo e pegue-o.

Para testar mais rapidamente durante o desenvolvimento, é possível usar o Meta Horizon Link e o botão **Play** do Editor. Essa opção exige um computador compatível e não substitui o teste final no headset, pois o desempenho é diferente.

## Prática

Adicione um segundo cubo mais distante, selecione-o e adicione o bloco **Distance Grab**. Execute a cena novamente e pegue o cubo sem se aproximar dele.

## Meça o desempenho

Aplicações interativas no Quest devem manter pelo menos **72 FPS**. Cada quadro precisa ser concluído dentro deste tempo:

| Taxa de atualização | Tempo por quadro |
| --- | --- |
| 72 Hz | 13,9 ms |
| 90 Hz | 11,1 ms |
| 120 Hz | 8,3 ms |

Use o [OVR Metrics Tool](https://developers.meta.com/horizon/documentation/unity/ts-ovr-best-practices/) para acompanhar o FPS e o tempo de CPU e de GPU no headset. Se o FPS cair, consulte o [fluxo básico de otimização](https://developers.meta.com/horizon/documentation/unity/po-perf-opt-mobile/) antes de alterar a cena.

## Se algo der errado

- **O headset não aparece em Run Device:** confira o cabo, a autorização de depuração USB e o **Device Manager** do MQDH.
- **A compilação falha ou o aplicativo não abre corretamente:** abra o **Project Setup Tool** e resolva os problemas da aba **Android**.
- **O cubo não reage:** confira se o **Interactions Rig** está na cena, se o cubo estava selecionado ao adicionar o bloco e se ele está ao alcance.
- **Apareceu um cubo a mais na cena:** nenhum objeto estava selecionado ao adicionar o bloco. Apague o cubo extra, selecione o seu e adicione o bloco novamente.

## Resultado e critérios de conclusão

- [ ] Montei a cena usando Building Blocks.
- [ ] Executei a cena no headset e peguei o cubo.
- [ ] Peguei o segundo cubo a distância.
- [ ] Medi o FPS e o tempo de CPU e de GPU no headset.

## Referências

- [Building Blocks](https://developers.meta.com/horizon/documentation/unity/bb-overview/)
- [Interaction SDK](https://developers.meta.com/horizon/documentation/unity/unity-isdk-interaction-sdk-overview/), para interações que os blocos não cobrem
- [Configuração de build](https://developers.meta.com/horizon/documentation/unity/unity-build/)

## Navegação

[← Anterior: Prepare o headset e o projeto para o Meta Quest](quest-preparacao.md)
