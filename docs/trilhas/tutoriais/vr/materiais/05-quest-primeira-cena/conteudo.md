# Crie sua primeira cena interativa no Quest

## Objetivo

Monte uma cena com o Interaction SDK, execute-a no headset e meça o desempenho.

## Pré-requisitos

Concluir [Prepare o headset e o projeto para o Meta Quest](../04-quest-preparacao/conteudo.md). Mantenha o headset conectado ao computador por USB.

## Monte a cena

1. Crie uma cena nova e apague a **Main Camera**, pois o Interaction SDK utiliza a sua própria câmera.
2. Clique com o botão direito na **Hierarchy** e escolha **Interaction SDK > Add OVR Comprehensive Interaction Rig**.
3. Se a cena não tiver um **OVRCameraRig**, clique em **Fix All** para o assistente criá-lo.
4. Selecione **Generate As Editable Copy**, informe o **Prefab Path** e clique em **Create**.
5. Selecione **OVRCameraRig** e, em **OVR Manager > Quest Features > General**, defina **Hand Tracking Support** conforme o projeto: **Controllers And Hands**, **Hands Only** ou **Controllers Only**.
6. Adicione um plano como chão e um cubo pequeno à frente da câmera, ao alcance da pessoa.
7. Clique com o botão direito no cubo e escolha **Interaction SDK > Add Ray Grab Interaction**.

## Execute no headset

1. Abra **File > Build Profiles** e selecione **Meta Quest**. Se essa plataforma não aparecer na sua versão da Unity, selecione **Android**.
2. Clique em **Switch Platform**, se necessário.
3. Em **Open Scene List**, adicione a cena.
4. Em **Run Device**, selecione o headset. Ele aparece apenas quando está conectado por USB.
5. Ative **Development Build** durante os testes e desative-o na versão final, pois essa opção pode afetar o desempenho.
6. Clique em **Build and Run** e escolha onde salvar o `.apk`.
7. No headset, aponte para o cubo e pegue-o.

Para testar mais rapidamente durante o desenvolvimento, é possível usar o Meta Horizon Link e o botão **Play** do Editor. Essa opção exige um computador compatível e não substitui o teste final no headset, pois o desempenho é diferente.

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
- **O cubo não reage:** confira se a cena tem o rig de interação e se a interação foi adicionada ao cubo.

## Resultado e critérios de conclusão

- [ ] Executei a cena no headset.
- [ ] Peguei o cubo usando a interação por raio.
- [ ] Medi o FPS e o tempo de CPU e de GPU no headset.

## Referências

- [Primeiros passos com o Interaction SDK](https://developers.meta.com/horizon/documentation/unity/unity-isdk-getting-started/)
- [Objetos que podem ser pegos com raio](https://developers.meta.com/horizon/documentation/unity/unity-isdk-create-ray-grabbable-object/)
- [Configuração de build](https://developers.meta.com/horizon/documentation/unity/unity-build/)
- [Building Blocks](https://developers.meta.com/horizon/documentation/unity/bb-overview/), uma alternativa para adicionar recursos prontos à cena

## Navegação

[← Anterior: Prepare o headset e o projeto para o Meta Quest](../04-quest-preparacao/conteudo.md)
