---
hide:
  - navigation
  - toc
---
# Introdução ao Servidor

## Objetivo

Conhecer os fundamentos básicos de Linux e Docker utilizados no servidor do LDTT, aprendendo a navegar pelo sistema, executar comandos e realizar a implantação de aplicações.

## Pré-requisitos

Concluir a [Introdução ao Git/GitHub](https://ldttfurb.github.io/LDTT_Capacitacao/materiais/git/introducao-git/) e possuir conhecimentos básicos sobre desenvolvimento web.

## O que você vai aprender

O servidor do laboratório utiliza **Linux** como sistema operacional e **Docker** para executar e gerenciar as aplicações.

É importante conhecer os comandos básicos dessas ferramentas para conseguir atualizar projetos, gerar builds, iniciar aplicações e identificar possíveis erros.

## 1. Linux — Comandos básicos

Linux é o sistema operacional utilizado no servidor. A maior parte das operações é realizada pelo terminal.

### Principais comandos

| Comando | Finalidade |
|---|---|
| `pwd` | Mostra o diretório atual |
| `ls -la` | Lista arquivos, incluindo os ocultos |
| `cd pasta` | Acessa um diretório |
| `cd ..` | Retorna ao diretório anterior |
| `mkdir pasta` | Cria um diretório |
| `cp origem destino` | Copia arquivos ou diretórios (com `-r`) |
| `mv origem destino` | Move ou renomeia arquivos |
| `rm arquivo` | Remove um arquivo |
| `cat arquivo` | Exibe o conteúdo de um arquivo |
| `nano arquivo` | Edita um arquivo pelo terminal |
| `chmod` | Altera permissões de arquivos |
| `sudo comando` | Executa um comando com permissões elevadas |

### Outros comandos importantes

| Comando | Finalidade |
|---|---|
| `ssh usuario@servidor` | Acessa um servidor remotamente |
| `git pull` | Atualiza o código do projeto |
| `ps aux` | Lista processos em execução |
| `df -h` | Consulta o espaço disponível em disco |
| `top` | Monitora processos e consumo de recursos |

### Material recomendado

- [Linux Journey](https://linuxjourney.com/) — Introdução aos fundamentos do Linux.
- [Linux — Curso em Vídeo](https://www.youtube.com/@CursoemVideo) — Aulas introdutórias de Linux.

## 2. Docker — Containers e aplicações

O Docker é uma ferramenta utilizada para executar aplicações em ambientes isolados chamados **containers**.

No laboratório, ele é utilizado para hospedar os projetos e facilitar sua implantação e manutenção.

### Conceitos básicos

- **Imagem:** contém os arquivos e as configurações necessários para executar uma aplicação.
- **Container:** instância em execução de uma imagem.
- **Dockerfile:** arquivo com as instruções para construir uma imagem.
- **Docker Compose:** ferramenta que permite configurar e executar múltiplos containers por meio de um arquivo YAML.

### Principais comandos

| Comando | Finalidade |
|---|---|
| `docker ps` | Lista containers em execução |
| `docker ps -a` | Lista todos os containers |
| `docker images` | Lista as imagens disponíveis |
| `docker build -t projeto:1.0 .` | Constrói uma imagem |
| `docker run -d --name projeto -p 8080:8080 projeto:1.0` | Cria e inicia um container |
| `docker stop projeto` | Para um container |
| `docker start projeto` | Inicia um container existente |
| `docker restart projeto` | Reinicia um container |
| `docker logs -f projeto` | Acompanha os logs do container |
| `docker exec -it projeto sh` | Acessa o terminal de um container |
| `docker rm projeto` | Remove um container parado |

### Docker Compose

Quando o projeto utiliza um arquivo `docker-compose.yml` ou `compose.yaml`, os principais comandos são:

| Comando | Finalidade |
|---|---|
| `docker compose build` | Constrói as imagens dos serviços |
| `docker compose up -d` | Cria e inicia os containers |
| `docker compose up -d --build` | Reconstrói as imagens e inicia os serviços |
| `docker compose ps` | Lista os serviços e seus estados |
| `docker compose logs -f` | Acompanha os logs |
| `docker compose down` | Para e remove os containers e redes do projeto |

### Material recomendado

- [Documentação oficial do Docker](https://docs.docker.com/get-started/) — Conceitos e primeiros passos.
- [Documentação do Docker Compose](https://docs.docker.com/compose/) — Configuração e execução de aplicações com múltiplos serviços.

## 3. Processo básico de implantação

O processo de atualização de um projeto no servidor geralmente segue estas etapas:

1. Acessar o servidor por SSH.
2. Navegar até o diretório do projeto.
3. Atualizar o código utilizando Git.
4. Construir a imagem Docker.
5. Iniciar ou recriar o container.
6. Verificar os logs e testar a aplicação.

### Exemplo utilizando Docker Compose

```bash
# Acessar o servidor
ssh usuario@servidor

# Entrar na pasta do projeto
cd caminho/do/projeto

# Atualizar o código
git pull

# Construir e iniciar os containers
docker compose up -d --build

# Verificar os containers
docker compose ps

# Acompanhar os logs
docker compose logs -f
```

### Exemplo utilizando Docker

Para projetos que não utilizam Docker Compose:

```bash
# Atualizar o código
git pull

# Construir a imagem
docker build -t projeto:1.0 .

# Parar e remover o container antigo, caso exista
docker stop projeto
docker rm projeto

# Criar e iniciar o novo container
docker run -d \
  --name projeto \
  --restart unless-stopped \
  -p 8080:8080 \
  projeto:1.0

# Verificar os logs
docker logs -f projeto
```

> **Atenção:** os comandos são exemplos. Os nomes dos containers, portas, diretórios e configurações variam conforme o projeto. Antes de atualizar uma aplicação do laboratório, consulte a documentação do projeto e confirme as configurações com a equipe. Evite remover volumes ou bancos de dados durante a implantação.

## Resultado e critérios de conclusão

- [ ] Compreendi os comandos básicos do Linux.
- [ ] Consigo navegar entre diretórios e manipular arquivos pelo terminal.
- [ ] Entendo a diferença entre imagem e container Docker.
- [ ] Sei construir uma imagem Docker.
- [ ] Sei iniciar, parar e reiniciar containers.
- [ ] Consigo consultar os logs de uma aplicação.
- [ ] Compreendo o processo básico de atualização e implantação de um projeto no servidor.
