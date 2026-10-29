# 09. Áudio: organização e reprodução

## Objetivo

Conheça o gerenciamento de sons, os materiais de áudio e a nomenclatura utilizada.

## Pré-requisitos

Concluir o tutorial 08: Interface: resolução, painéis e desempenho.

## 1. Gerenciamento de áudio

Um **Sound Manager** é um gerenciador que organiza pedidos de reprodução de sons. Por exemplo, o código de uma coleta pode solicitar um efeito sonoro a esse gerenciador. Verifique como o projeto já faz isso e como os sistemas se relacionam antes de propor uma nova solução.

1. Localize uma música e um efeito sonoro utilizados no jogo.
2. Identifique onde a reprodução é solicitada.
3. Verifique se há um gerenciador responsável por esse fluxo.
4. Observe como ele se relaciona com as cenas e com outros sistemas.

**Estudo indicado:** [Sound Manager — EN](https://youtu.be/QL29aTa7J5Q).

## 2. Funcionalidades de áudio da Unity

Para acompanhar a reprodução, reconheça dois elementos: o **AudioClip** é o recurso que contém o som, e o **AudioSource** é o componente que o reproduz na cena. O material abaixo serve de apoio para estudar os recursos empregados pelo projeto e discutir ajustes com a equipe.

**Estudo indicado:** [Funcionalidades de áudio — EN](https://youtu.be/B9yxkJuHLek). Ao estudar, anote quais recursos também aparecem no projeto e quais dúvidas você precisa discutir com a equipe.

## 3. Relacione com a nomenclatura

| Categoria | Convenção | Exemplo |
| --- | --- | --- |
| Efeito sonoro | `SFX_`, seguido de objeto e ação | `SFX_CoinDrop` |
| Música | `OST_` | `OST_MenuTheme` |

Evite renomear assets já referenciados apenas para cumprir um exercício. Registre divergências e combine a mudança com o responsável.

## 4. Exercício

Execute um fluxo que contenha música e efeito sonoro. Identifique o arquivo e a ação que inicia cada som. Por exemplo: a música começa ao abrir o menu e o efeito toca ao coletar uma moeda. Depois, procure o componente ou o trecho de código responsável pela reprodução. Registre se o comportamento observado corresponde ao esperado. Se o projeto não tiver áudio, faça a análise com um exemplo do material indicado em ambiente de treinamento.

## Resultado e critérios de conclusão

- [ ] Localizei ou estudei uma música e um efeito sonoro.
- [ ] Identifiquei como a reprodução é acionada.
- [ ] Relacionei os arquivos às convenções SFX_ e OST_.

## Navegação

[← Anterior: Interface: resolução, painéis e desempenho](../08-interface-e-desempenho/conteudo.md)

[Próximo: Implemente e teste sua primeira alteração →](../10-primeira-alteracao/conteudo.md)
