# Execute a cena de exemplo no celular

## Objetivo

Gere o aplicativo Hello Cardboard, teste-o no visor e estude a interação pelo olhar.

## Pré-requisitos

Concluir [Prepare o projeto para o Google Cardboard](cardboard-preparacao.md). Tenha um cabo USB de dados e ative a depuração USB nas [opções do desenvolvedor do celular](https://developer.android.com/studio/debug/dev-options).

## Prepare a cena

1. Abra a cena `HelloCardboard`, em `Assets/Samples/Google Cardboard/<versão>/Hello Cardboard/Scenes`.
2. Em **File > Build Profiles**, adicione a cena aberta à lista de cenas.
3. Crie uma layer chamada `Interactive`.
4. Coloque o objeto **Treasure** e seus filhos nessa layer.
5. Selecione **Player > Camera** e, no componente **CardboardReticlePointer**, defina **Reticle Interaction Layer Mask** como `Interactive`.

Sem essa configuração, a retícula (o ponto de mira no centro da visão) não reconhece o objeto.

## Gere e execute o aplicativo

1. Conecte o celular ao computador e autorize a depuração USB.
2. Em **File > Build Profiles**, selecione o celular em **Run Device**.
3. Clique em **Build and Run** e escolha onde salvar o `.apk`.
4. Se o aplicativo pedir, leia o QR code do visor Cardboard com a câmera do celular.
5. Coloque o celular no visor e olhe para o objeto Treasure.

Para recentralizar a cena de exemplo, mantenha o botão do visor pressionado por pelo menos três segundos e solte.

## Prática

Abra os scripts usados pela cena e identifique como o objeto reage quando a retícula entra nele, sai dele ou quando o botão é acionado. Depois, adicione um novo objeto à layer `Interactive` e faça-o reagir da mesma forma.

## Se algo der errado

- **O celular não aparece em Run Device:** confira o cabo, a autorização de depuração USB e atualize a lista de dispositivos.
- **O objeto não reage:** confira a layer do objeto e dos filhos e o campo **Reticle Interaction Layer Mask**.
- **A compilação falha nas dependências:** compare os arquivos Gradle com o [guia oficial](https://developers.google.com/cardboard/develop/unity/quickstart), pois as versões podem mudar entre versões do plugin.
- **O aplicativo fecha ao abrir:** gere o aplicativo com **Development Build** ativado e examine os registros de execução.

## Resultado e critérios de conclusão

- [ ] Executei o Hello Cardboard no celular com o visor.
- [ ] Recentralizei a cena e interagi com o objeto.
- [ ] Adicionei um novo objeto interativo.

## Referências

- [Guia inicial do Cardboard para Unity](https://developers.google.com/cardboard/develop/unity/quickstart)

## Navegação

[← Anterior: Prepare o projeto para o Google Cardboard](cardboard-preparacao.md)
