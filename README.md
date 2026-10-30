# LDTT HUB de Capacitação

Site: https://ldttfurb.github.io/LDTT_Capacitacao/

## Como adicionar um tutorial

1. O bolsista escreve **um único `.md`**, com `# Título` e, se possível, `## Objetivo` seguido de um parágrafo.
2. O responsável publica o arquivo em `docs/materiais/<area>/<nome>.md`. Não são necessários `index.md`, metadados YAML ou pastas individuais por tutorial.
3. O tutorial já aparece em **Novos tutoriais** na trilha da área. Para incluí-lo na árvore, acrescente `- area/nome` em `roteiros/<trilha>.md`. Cada grupo de **dois espaços** de recuo cria uma relação de filho.
4. Faça commit na branch `main`. O workflow gera os cards, os links e o site.

### Estrutura

- `docs/materiais/` — tutoriais individuais, somente arquivos `.md`.
- `roteiros/` — listas de IDs de tutoriais e suas conexões. Um arquivo por trilha.
- `docs/trilhas/tutoriais/` — metadados e páginas de apresentação das trilhas.
- `scripts/gerar_arvores.py` — gera as árvores automaticamente, sem duplicar tutoriais.
- `scripts/gerar_cards.py` — gera a página com os cards de trilhas.
- `scripts/redirecionamentos_antigos.json` — preserva no site os endereços dos tutoriais anteriores à migração; não precisa ser editado ao adicionar tutoriais.

Um tutorial pode estar em várias árvores. Por exemplo, `git/introducao-git` pertence à trilha Git e também pode ser apresentado na árvore da Unity.

Consulte **Enviar Tutorial** no próprio site para as instruções completas, incluindo a criação de uma nova área.

## Ao instalar esta atualização em um clone antigo

**Atenção:** copiar o ZIP por cima da pasta do Git **não remove os arquivos antigos**. Antes de commitar, apague estas duas pastas antigas do clone (elas foram substituídas por `docs/materiais/`):

- `docs/trilhas/tutoriais/unity/materiais/`
- `docs/trilhas/tutoriais/vr/materiais/`

As pastas acima eram compostas pelos arquivos `index.md` e `conteudo.md` dos 18 tutoriais migrados. Se você adicionou outros arquivos ali desde que gerou o ZIP original, faça backup deles antes de apagar.

**Não apague a pasta `.git`.** Depois de copiar o conteúdo do ZIP, confirme que o Git reconheceu as exclusões e os arquivos novos usando `git status`. Use `git add -A` para incluir também as exclusões, antes do commit.

Os endereços públicos antigos dos 18 tutoriais serão redirecionados automaticamente pelo script durante a publicação, mesmo após as pastas antigas terem sido removidas do repositório.
