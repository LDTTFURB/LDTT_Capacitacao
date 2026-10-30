# Prepare o headset e o projeto para o Meta Quest

## Objetivo

Ative o modo de desenvolvedor no headset e configure um projeto Unity com o Meta XR SDK.

## Pré-requisitos

Concluir [Introdução à VR](introducao-vr.md). Você também precisará de:

- Um headset Meta Quest, combinado com a equipe.
- Um cabo USB de dados. Cabos usados apenas para carga não funcionam.
- O celular com o aplicativo Meta Horizon pareado ao headset.
- Uma conta de desenvolvedor da Meta. A Meta exige idade mínima de 18 anos para ativar o modo de desenvolvedor.

As telas e os menus da Meta mudam com frequência. Se algo estiver diferente, consulte os links em [Referências](#referencias).

## Ative o modo de desenvolvedor

1. Crie ou acesse uma equipe no [painel de desenvolvedor da Meta](https://developers.meta.com/horizon/manage/).
2. Verifique a conta, por SMS com verificação em duas etapas ou por um método de pagamento. Use a sua própria conta e não compartilhe esses dados.
3. No aplicativo Meta Horizon, abra as configurações do headset e ative **Developer Mode**.
4. Conecte o headset ao computador. No headset, abra **Settings > Developer**, ative **MTP Notification** e selecione **Always allow from this computer** para permitir a depuração USB.
5. Instale o [Meta Quest Developer Hub](https://developers.meta.com/horizon/documentation/unity/ts-mqdh-getting-started/) (MQDH) e entre com a mesma conta.
6. No **Device Manager** do MQDH, confirme que o headset aparece como ativo.

## Crie o projeto

1. No Unity Hub, instale a versão do Editor indicada pela equipe, com o módulo **Android Build Support** e as opções **OpenJDK** e **Android SDK & NDK Tools**.
2. Ainda no Unity Hub, crie um novo projeto com essa versão, usando o modelo **Universal 3D**.
3. Com o projeto aberto, acesse o [Meta XR All-in-One SDK](https://assetstore.unity.com/packages/tools/integration/meta-xr-all-in-one-sdk-269657) na Unity Asset Store e clique em **Add to My Assets**.
4. Clique em **Open in Unity**. No **Package Manager**, selecione o SDK e clique em **Install**.
5. Se a Unity pedir para atualizar o **OVRPlugin** ou para trocar a Graphics API para Direct3D11, aceite e deixe o Editor reiniciar.

## Ajuste as configurações

1. Abra **Edit > Project Settings > XR Plug-in Management**. Se a ferramenta não estiver instalada, clique em **Install XR Plugin Management**.
2. Nas abas **Windows, Mac, Linux** e **Android**, selecione **OpenXR**. Evite o plugin **Oculus**, que está descontinuado.
3. Em **XR Plug-in Management > OpenXR**, na seção **OpenXR Feature Groups**, ative **Meta XR** para **Standalone** e **Android**.
4. Abra **Window > Meta > Tools > Project Setup Tool**.
5. Nas abas **Standalone** e **Android**, clique em **Fix All** para os problemas pendentes.
6. Revise os itens recomendados e faça os ajustes manuais indicados pela ferramenta.

## Resultado e critérios de conclusão

- [ ] Ativei o modo de desenvolvedor e o headset aparece no MQDH.
- [ ] Criei o projeto no Unity Hub e instalei o Meta XR SDK.
- [ ] Configurei o projeto para usar OpenXR.
- [ ] Resolvi os problemas apontados pelo Project Setup Tool.

## Referências

- [Configuração do projeto Unity](https://developers.meta.com/horizon/documentation/unity/unity-project-setup/)
- [Instalação dos pacotes Meta XR](https://developers.meta.com/horizon/documentation/unity/unity-package-manager/)
- [Ativação do modo de desenvolvedor](https://developers.meta.com/horizon/documentation/android-apps/enable-developer-mode/)

## Navegação

[← Anterior: Introdução à VR](introducao-vr.md)

[Próximo: Crie sua primeira cena interativa no Quest →](quest-primeira-cena.md)
