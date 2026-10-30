# Prepare o projeto para o Google Cardboard

## Objetivo

Instale o Cardboard XR Plugin e configure um projeto Unity para gerar um aplicativo Android.

## Pré-requisitos

Concluir [Introdução à VR](introducao-vr.md). Você também precisará de:

- Unity 6000.0.23f1 ou mais recente (consultar versão atual utilizada pela equipe), com o módulo **Android Build Support**.
- Git instalado e disponível no `PATH` do sistema.
- Um celular Android 8.0 ou mais recente e um visor Cardboard.

Esta página apresenta a configuração para Android. Para iOS, consulte o [guia oficial](https://developers.google.com/cardboard/develop/unity/quickstart). Como os requisitos podem mudar entre versões do plugin, confira esse guia caso algum valor abaixo não funcione.

## Instale o plugin

1. Crie um projeto 3D de treinamento na Unity.
2. Abra **Window > Package Manager**.
3. Clique em **+ > Add package from git URL** e informe:

    ```text
    https://github.com/googlevr/cardboard-xr-plugin.git
    ```

4. Na seção **Samples** do pacote, clique em **Import into Project**.

## Configure o projeto para Android

Em **File > Build Profiles**, selecione **Android** e clique em **Switch Platform**. Depois, abra **Edit > Project Settings > Player** e ajuste:

| Seção | Configuração | Valor |
| --- | --- | --- |
| Resolution and Presentation | Default Orientation | Landscape Left ou Landscape Right |
| Resolution and Presentation | Optimized Frame Pacing | Desativado |
| Other Settings | Graphics APIs | OpenGLES3 |
| Other Settings | Minimum API Level | Android 8.0 "Oreo" (API 26) ou superior |
| Other Settings | Target API Level | API 35 ou superior |
| Other Settings | Scripting Backend | IL2CPP |
| Other Settings | Target Architectures | ARM64 |
| Other Settings | Internet Access | Require |
| Other Settings | Active Input Handling | Input System Package (New) |
| Other Settings | Application Entry Point | Activity (desmarque GameActivity) |
| Other Settings | Package Name | Nome do pacote, como `br.furb.ldtt.meuprojeto` |

## Adicione as dependências do Android

1. Em **Player > Publishing Settings**, na seção **Build**, ative **Custom Main Gradle Template** e **Custom Gradle Properties Template**.
2. Na seção `dependencies` de `Assets/Plugins/Android/mainTemplate.gradle`, adicione:

    ```text
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.gms:play-services-vision:20.1.3'
    implementation 'com.google.android.material:material:1.12.0'
    implementation 'com.google.protobuf:protobuf-javalite:3.19.4'
    ```

3. Em `Assets/Plugins/Android/gradleTemplate.properties`, adicione:

    ```text
    android.enableJetifier=true
    android.useAndroidX=true
    ```

## Ative o Cardboard

Abra **Edit > Project Settings > XR Plug-in Management**. Na aba do Android, em **Plug-in Providers**, selecione **Cardboard XR Plugin**.

## Resultado e critérios de conclusão

- [ ] Instalei o plugin e importei o exemplo Hello Cardboard.
- [ ] Configurei o projeto para Android.
- [ ] Adicionei as dependências e ativei o Cardboard XR Plugin.

## Navegação

[← Anterior: Introdução à VR](introducao-vr.md)

[Próximo: Execute a cena de exemplo no celular →](cardboard-primeira-execucao.md)
