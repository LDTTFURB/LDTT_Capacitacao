# 01. Preparação do ambiente e acessos

## Objetivo

Prepare suas contas, ferramentas e a versão da Unity utilizada no projeto.

## Pré-requisitos

Ter um computador disponível e saber quem pode orientar seus primeiros passos no laboratório. Neste tutorial, integração significa esse período de preparação e familiarização com a equipe e o projeto.

## Conheça o laboratório

Converse com o responsável pelo projeto para identificar:

- Em qual projeto você irá trabalhar e qual é seu objetivo.
- Quem poderá acompanhar sua integração e revisar suas entregas.
- Qual repositório deve ser utilizado e quais acessos são necessários.
- Qual versão da Unity e quais módulos de plataforma o projeto exige.
- Como as tarefas são distribuídas e onde as dúvidas devem ser registradas.

Se estiver usando uma máquina da FURB, verifique o que já está instalado. Quando uma instalação ou atualização exigir permissão de administrador, procure o professor Dalton ou outro professor responsável, conforme orientado no guia.

**Comunicação faz parte do trabalho:** pergunte quando tiver dúvidas, compartilhe impedimentos e avise antes de alterar algo que possa afetar seus colegas.

## Ferramentas e configuração

| Ferramenta | Para que serve no trabalho diário |
| --- | --- |
| Unity Editor | Editar cenas, configurar objetos, programar comportamentos e executar o jogo. |
| Unity Hub | Gerenciar projetos e instalações do Unity Editor. |
| C\# | Linguagem utilizada para programar os comportamentos dos projetos. |
| Git | Registrar alterações e manter o histórico de desenvolvimento. |
| GitHub | Hospedar os repositórios e organizar a colaboração e a revisão de alterações. |
| GitHub Desktop | Trabalhar visualmente com operações de Git e GitHub. |
| IDE (ambiente de desenvolvimento) | Escrever código C\# e investigar erros com ferramentas de navegação e depuração. Depurar é acompanhar a execução do código para entender seu comportamento. |

### Prepare suas contas e acessos

1. Crie ou acesse sua [conta Unity ID](https://login.unity.com/en/sign-in).
2. Crie ou acesse sua conta no GitHub.
3. Solicite ao professor Dalton acesso à organização e ao repositório do projeto no GitHub.
4. Aceite o convite recebido e confirme que consegue visualizar o repositório.

### Instale o Unity Hub e a versão correta do Editor

1. Instale o [Unity Hub](https://unity.com/pt/download).
2. Entre com sua conta Unity.
3. Antes de instalar o Editor, confira a versão utilizada pelo projeto. Você pode consultar o README, perguntar à equipe ou, após clonar o repositório, abrir o arquivo `ProjectSettings/ProjectVersion.txt` em um editor de texto.
4. Instale essa versão pelo Unity Hub, junto dos módulos de plataforma indicados pela equipe. Esses módulos dão suporte à plataforma para a qual o jogo será gerado, como Android.

### Configure a IDE

O guia recomenda o **Visual Studio**, mas permite alternativas compatíveis com C\# e Unity, como **Visual Studio Code** e **JetBrains Rider**.

1. Verifique se a IDE escolhida está instalada e possui suporte ao desenvolvimento com Unity.
2. Nas preferências do Unity Editor, localize a configuração de ferramentas externas e selecione o editor de scripts. A localização e o nome dessa opção podem variar conforme a versão e o sistema operacional.
3. Quando o projeto estiver aberto, dê dois cliques em um script C\# na janela Project.
4. Confirme que o arquivo abre na IDE e que ela reconhece os tipos da Unity.

Não suponha que a IDE foi instalada automaticamente com o Editor: confira a instalação antes de começar.

### Prepare o GitHub Desktop

1. Instale o [GitHub Desktop](https://desktop.github.com/download/).
2. Entre com sua conta do GitHub.
3. Configure seu nome e e-mail para identificar a autoria dos commits, que são registros de alterações no histórico do Git.
4. Se preferir usar Git pelo terminal, verifique também se o Git está instalado.

> A abertura de scripts para validar a IDE será feita no tutorial 04, após clonar e abrir o projeto.

## Resultado e critérios de conclusão

- [ ] Identifiquei meu projeto e quem pode me orientar.
- [ ] Tenho acesso ao repositório e às contas necessárias.
- [ ] Instalei ou solicitei as ferramentas e confirmei a versão do Editor.

## Navegação

[Próximo: Fundamentos de C\#, Unity e materiais de estudo →](../02-fundamentos-e-estudos/conteudo.md)
