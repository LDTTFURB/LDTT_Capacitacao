# Introdução à VR

## Objetivo

Entenda os conceitos básicos de Realidade Virtual e identifique qual ramo da trilha seguir.

## Pré-requisitos

Ter a Unity instalada e conhecer o Editor. Se ainda não conhece, comece por [Introdução geral](../../../unity/materiais/01-preparacao-do-ambiente/conteudo.md) e [Introdução à Unity](../../../unity/materiais/04-primeira-execucao-na-unity/conteudo.md), da trilha Unity.

## O que você vai aprender

Em uma aplicação de VR, a pessoa enxerga uma cena 3D em um visor, e a imagem acompanha o movimento da cabeça. Por isso, a experiência depende de uma imagem estável e de interações que funcionem sem teclado e sem mouse.

## Conceitos básicos

- **Headset:** visor usado na cabeça. No Cardboard, é um suporte de papelão com lentes e um celular.
- **Rastreamento 3DoF:** detecta apenas a rotação da cabeça. É o caso do Cardboard.
- **Rastreamento 6DoF:** detecta a rotação e a posição da cabeça. É o caso do Quest.
- **Taxa de quadros (FPS):** quantidade de imagens geradas por segundo.
- **Recentralizar:** redefinir qual direção é a "frente" da pessoa.

## Escolha o ramo

| | Google Cardboard | Meta Quest |
| --- | --- | --- |
| Equipamento | Óculos Cardboard e celular | Headset Meta Quest |
| Onde a aplicação é executada | No celular | No próprio headset |
| Movimento detectado | Rotação da cabeça | Rotação e posição da cabeça e das mãos ou controles |
| Interação típica | Olhar para um objeto e usar o botão do visor | Apontar, tocar e pegar objetos |
| Pacote usado na Unity | Cardboard XR Plugin | Meta XR SDK |

Confirme com a equipe qual plataforma o seu projeto utiliza e quais equipamentos estão disponíveis.

## Conforto e desempenho

Estas orientações valem para as duas plataformas:

- **Priorize a taxa de quadros.** Quedas de FPS são percebidas com facilidade e podem causar desconforto.
- **Não mova a câmera sem a ação da pessoa.** Evite acelerações, tremores e rotações forçadas.
- **Mantenha textos e botões legíveis.** Teste no equipamento, pois a tela do computador não mostra como a interface fica no visor.
- **Faça pausas.** Interrompa o teste se sentir tontura ou enjoo.
- **Teste em um local seguro.** Mantenha a área livre de obstáculos e peça que um colega acompanhe quando necessário.

## Resultado e critérios de conclusão

- [ ] Sei explicar a diferença entre 3DoF e 6DoF.
- [ ] Identifiquei a plataforma e o equipamento do meu projeto.

## Navegação

**Próximos:**

- [Prepare o projeto para o Google Cardboard →](../02-cardboard-preparacao/conteudo.md)
- [Prepare o headset e o projeto para o Meta Quest →](../04-quest-preparacao/conteudo.md)
