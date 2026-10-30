# Prepare o headset e o projeto para o Meta Quest

## Objetivo

Ative o modo de desenvolvedor no headset e configure um projeto Unity com o Meta XR SDK.

## Pré-requisitos

Concluir [Introdução à VR](../01-introducao-a-vr/conteudo.md). Você também precisará de:

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

1. No MQDH, crie um novo projeto Unity e escolha a versão do Editor indicada pela equipe.
2. Na seção de configuração, defina **XR Plugin** como **OpenXR** e **SDKs** como **All**. Essa opção instala os pacotes do Meta XR All-in-One SDK.
3. Abra o projeto. No Windows, se a Unity pedir para trocar a Graphics API para Direct3D11, selecione **Yes, Switch and Restart**.

Evite o plugin **OculusXR**, que está descontinuado.

## Ajuste as configurações

1. Abra **Edit > Project Settings > XR Plug-in Management > OpenXR**.
2. Em **OpenXR Feature Groups**, ative **Meta XR** para **Standalone** e **Android**.
3. Abra **Window > Meta > Tools > Project Setup Tool**.
4. Nas abas **Standalone** e **Android**, clique em **Fix All** para os problemas pendentes.
5. Revise os itens recomendados e faça os ajustes manuais indicados pela ferramenta.

## Resultado e critérios de conclusão

- [ ] Ativei o modo de desenvolvedor e o headset aparece no MQDH.
- [ ] Criei o projeto com OpenXR e o Meta XR SDK.
- [ ] Resolvi os problemas apontados pelo Project Setup Tool.

## Referências

- [Configuração do projeto Unity](https://developers.meta.com/horizon/documentation/unity/unity-project-setup/)
- [Ativação do modo de desenvolvedor](https://developers.meta.com/horizon/documentation/android-apps/enable-developer-mode/)

## Navegação

[← Anterior: Introdução à VR](../01-introducao-a-vr/conteudo.md)

[Próximo: Crie sua primeira cena interativa no Quest →](../05-quest-primeira-cena/conteudo.md)
