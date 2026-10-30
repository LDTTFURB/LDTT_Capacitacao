# Introdução à Unity

## Objetivo

Abra o projeto, execute a cena inicial e reconheça seus principais elementos.

## Pré-requisitos

Concluir [Introdução geral](introducao-geral.md) e [Introdução ao Git/GitHub](../git/introducao-git.md), da ramificação Git/GitHub. Tenha a pasta do projeto no computador e a versão correta do Editor instalada.

## O que você vai aprender

A Unity é o motor de jogo usado no projeto. O Editor reúne as ferramentas para organizar cenas, configurar objetos e executar o jogo. Nesta introdução, você abrirá o projeto e conhecerá suas janelas principais. Depois, os conteúdos filhos ajudam a estudar interface, áudio e uma primeira alteração prática.


## Abra no Unity Hub

1. No Unity Hub, adicione o projeto existente a partir do disco.
2. Selecione a pasta que contém `Assets`, `Packages` e `ProjectSettings`. Em alguns repositórios, ela fica dentro de uma subpasta.
3. Confira a versão do Editor associada ao projeto.
4. Abra o projeto e aguarde a preparação dos recursos do projeto (assets) e dos pacotes, que reúnem funcionalidades e dependências usadas pelo projeto.
5. Localize a cena inicial indicada no README ou pela equipe.
6. Abra a cena e execute o projeto com o botão **Play**.

A primeira abertura pode demorar mais. Antes de modificar qualquer código, verifique se o projeto já funciona na sua máquina e registre eventuais erros existentes.

## Explore o Editor e o projeto

### Reconheça as janelas principais

| Janela | O que observar |
| --- | --- |
| Hierarchy | Os GameObjects presentes na cena e sua organização em objetos pais e filhos. Um objeto filho aparece dentro de outro na Hierarchy. |
| Scene | O espaço de edição e posicionamento dos objetos. |
| Game | A visualização produzida pelo jogo durante a execução. |
| Inspector | Os componentes e as propriedades do objeto ou asset selecionado. |
| Project | Os arquivos e assets disponíveis no projeto. |
| Console | As mensagens, os avisos e os erros de compilação ou execução. |

### Identifique os conceitos básicos

- **Cena:** reúne objetos e configurações de uma parte do jogo, como um menu ou uma fase.
- **GameObject:** objeto da cena que recebe componentes.
- **Componente:** define dados ou comportamentos associados a um GameObject.
- **Script:** arquivo de código; muitos comportamentos de objetos são implementados em componentes C\#.
- **Prefab:** asset reutilizável que armazena uma configuração de objetos e componentes.
- **Asset:** recurso do projeto, como uma imagem, um áudio, um material, uma cena ou um script.

### Faça uma exploração guiada

1. Execute o fluxo principal do jogo e observe como o usuário interage com ele.
2. Selecione um objeto na Hierarchy e examine seus componentes no Inspector.
3. Encerre o modo Play e abra um script desse objeto com dois cliques no componente ou no arquivo da janela Project. Identifique um trecho que ajude a explicar o comportamento observado; peça apoio a um colega se precisar.
4. Identifique onde ficam cenas, scripts, prefabs, imagens e áudios.
5. Pergunte quais cenas e sistemas estão em desenvolvimento por outros colegas.

> Alterações feitas durante o modo Play podem não permanecer após encerrar a execução. Para uma mudança persistente, saia do Play, aplique a alteração no modo de edição e salve o que foi modificado.

## Prática de fundamentos e material de apoio

Em um projeto de treinamento, crie uma cena com um GameObject, associe um script e adicione um campo público simples, como um número inteiro de pontos, para editá-lo no Inspector. Observe o componente Transform, que guarda posição, rotação e escala. Use um prefab para estudar como uma configuração de objetos pode ser reutilizada. Compare o exercício com um objeto do projeto do laboratório.

**Estudo indicado:** [Vídeo de introdução à Unity](https://www.youtube.com/watch?v=pyw2HTsdkEQ).

**Curso introdutório:** [Unity Essentials](https://learn.unity.com/pathway/unity-essentials). Use-o para praticar os conceitos básicos do Editor em um ambiente de treinamento.

### Cursos de apoio: Unity 2D e 3D

Escolha com a equipe o curso mais relacionado ao seu projeto e à sua experiência:

- [Curso Unity 2D — Udemy](https://www.udemy.com/share/101WYy3@Sm21KC48vdtREKT4CVhsnhoZu4FNxubjR2yMmTUOQam2YxQsJTipt9RtDnAB9rKb/).
- [Curso Unity 3D — Udemy](https://www.udemy.com/share/101XCe3@WvQmbY0TW23Kt_f-F9FTMazvUdWBKBYG8ID6XMu-IcgFexio5gRQcqBqWqCXHeQe/).

Não é necessário concluir os dois cursos para seguir a trilha. Alterne os trechos que ajudam na sua tarefa com exercícios em um projeto de treinamento.

## Resultado e critérios de conclusão

- [ ] Abri o projeto com a versão correta.
- [ ] Executei a cena inicial ou registrei um impedimento para a equipe.
- [ ] Localizei cenas, scripts e prefabs e consegui abrir um script na IDE.

## Navegação

[← Anterior: Introdução geral](introducao-geral.md)

**Próximos:**

- [Interface: resolução, painéis e desempenho →](interface-e-desempenho.md)
- [Áudio: organização e reprodução →](audio.md)
- [Implemente e teste sua primeira alteração →](primeira-alteracao.md)
