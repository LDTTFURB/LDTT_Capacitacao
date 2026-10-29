# Nomenclatura e organização de arquivos

> Ramificação: **C\# e boas práticas**.

## Objetivo

Use os padrões de nomes de código e recursos (assets) do LDTT e entenda como preservar as referências entre os arquivos do projeto.

## Pré-requisitos

Revisar [Fundamentos de C\# e plano de estudos](../02-fundamentos-e-estudos/conteudo.md) e concluir [Primeira execução e exploração do projeto](../04-primeira-execucao-na-unity/conteudo.md). Para comparar os nomes, você precisa reconhecer variáveis, classes e os arquivos principais do projeto.

## 1. Regras gerais

Use nomes **em inglês** que indiquem a função do elemento. Por exemplo, `score` comunica melhor uma pontuação do que `value`. Para classes e tipos, comece com maiúscula; para variáveis públicas e locais, comece com minúscula. Em nomes compostos, cada palavra seguinte começa com maiúscula. Quando números fizerem parte do nome, siga o formato dos exemplos do laboratório: `01`, `02`.

O formato de `GameManager` é chamado de **PascalCase**; o de `arrayAmount`, de **camelCase**. Nas tabelas abaixo, prefixo é uma parte acrescentada ao início do nome, e sufixo é uma parte acrescentada ao final.

## 2. Código e prefabs

| Elemento | Convenção do laboratório | Exemplos |
| --- | --- | --- |
| Scripts e prefabs de interface | Prefixo `UI` | `UIManager`, `UICompiler` |
| Scripts e prefabs de gerenciamento | Sufixo `Manager` | `GameManager`, `UIManager` |
| ScriptableObject | Prefixo `Scriptable` | `ScriptableItem`, `ScriptableCard` |
| Enum | Prefixo `E` | `EDirection`, `EColor` |
| Interface | Prefixo `I` | `ICharacter`, `ICollectable` |
| Delegate | Sufixo `Delegate` | `AttackDelegate` |
| Evento | Prefixo `On` | `OnHealthChanged`, `OnHit` |
| Variável pública ou local | Primeira letra minúscula; palavras seguintes com inicial maiúscula | `amount`, `arrayAmount` |
| Variável privada ou protegida | Prefixo `_` e primeira letra minúscula | `_amount`, `_arrayAmount` |
| Variável que referencia um prefab | Sufixo `Prefab`, respeitando também a visibilidade | `fishPrefab`, `_itemPrefab` |
| Método assinante de evento | Nome do publicador, `_` e nome do evento | `Furbot_OnHealthChanged`, `Character_OnHit` |

Um evento é uma notificação enviada pelo código, e o método assinante é o método que responde a ela. Por exemplo, `OnHit` pode ser o evento e `Character_OnHit` o método que reage a ele. O material [C\#: contratos, eventos e refatoração](../06-csharp-e-refatoracao/conteudo.md) explica essa relação com mais detalhes.

## 3. Animação, sprites e áudio

| Asset ou script | Convenção | Exemplo |
| --- | --- | --- |
| AnimationClip | Sufixo `_AnimClip` | `Furbot_Right_AnimClip` |
| Asset de controlador de animação | Sufixo `_AnimController` | `Furbot_AnimController` |
| Script de controle de animação | Sufixo `AnimController` | `CharacterAnimController` |
| Sprite | Prefixo `S_` e dimensões originais no final | `S_Inventory_1024x1024` |
| Sprite de interface | Prefixo `S_UI_` e dimensões originais no final | `S_UI_FurbotHead_256x256` |
| Efeito sonoro | Prefixo `SFX_`; nome com objeto relacionado e ação | `SFX_CoinDrop` |
| Música | Prefixo `OST_` | `OST_MenuTheme` |

## 4. Cuidados com arquivos Unity

As orientações abaixo complementam o guia para o trabalho em equipe:

- Preserve os arquivos `.meta`: eles guardam identificadores e configurações usados nas referências entre assets. Uma referência é a ligação que permite, por exemplo, a um componente encontrar a imagem ou o áudio que utiliza.
- Prefira mover e renomear assets pela janela Project da Unity.
- Confira o `.gitignore` do repositório antes de adicionar arquivos. Esse arquivo informa ao Git quais arquivos e pastas devem ser ignorados. Pastas geradas, como `Library`, `Temp`, `Logs` e `Obj`, normalmente não devem ser versionadas.
- Combine com os colegas antes de editar a mesma cena ou o mesmo prefab, reduzindo a chance de conflitos.
- Evite misturar sua tarefa com reorganizações amplas ou alterações de configuração sem relação com ela.
- Não inclua senhas, tokens ou credenciais nos arquivos enviados ao repositório.

## 5. Exercício de revisão

1. Escolha um script, uma variável privada, um prefab, um sprite e um áudio do projeto, quando existirem.
2. Compare seus nomes com as tabelas acima.
3. Anote desvios e dúvidas para discutir com o responsável.
4. Consulte os [padrões do laboratório](https://docs.google.com/document/d/1GngSO6ZCpCthvPQP6ri8Rm5cNR_9k4ME3vWAX3B4tyk/edit?pli=1&tab=t.0) e a [convenção de nomenclatura](https://docs.google.com/document/d/1bncqkJJxBkCD1ro23AX1pr1rMplbuYwO8Ko27TO_kCI/edit?tab=t.0).
5. Não renomeie arquivos e tipos em massa para concluir o exercício. Uma mudança de nome pode afetar referências e trabalho de outros colegas.

## Resultado e critérios de conclusão

- [ ] Revisei as regras de nomes em inglês e os prefixos e sufixos.
- [ ] Comparei exemplos do projeto com a tabela de nomenclatura.
- [ ] Anotei as diferenças entre os nomes encontrados e as convenções para confirmar com a equipe.
- [ ] Entendi os cuidados com arquivos .meta e assets compartilhados.

## Navegação

[← Voltar ao mapa da trilha](../../conteudo.md)

[← Anterior nesta ramificação: Fundamentos de C\# e plano de estudos](../02-fundamentos-e-estudos/conteudo.md)

[Próximo nesta ramificação: C\#: contratos, eventos e refatoração →](../06-csharp-e-refatoracao/conteudo.md)
