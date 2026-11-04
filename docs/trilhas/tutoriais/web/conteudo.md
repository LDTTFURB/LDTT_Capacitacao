---
hide:
  - navigation
  - toc
---
# Introdução ao Desenvolvimento Web

## Objetivo

Conhecer os fundamentos do desenvolvimento web utilizados nos projetos do LDTT, compreendendo o funcionamento das aplicações, a comunicação entre frontend e backend e as principais tecnologias utilizadas pelo laboratório.

## Pré-requisitos

Concluir a introdução ao Git/GitHub e possuir conhecimentos básicos de lógica de programação.

É recomendado conhecer os fundamentos de HTML, CSS, JavaScript e programação orientada a objetos (POO).

## Tecnologias utilizadas

Atualmente, os projetos web do laboratório utilizam principalmente as seguintes tecnologias:

| Tecnologia  | Finalidade |
|---|---|
| Angular | Desenvolvimento do frontend |
| Java | Linguagem utilizada no backend |
| Spring Boot | Framework para desenvolvimento do backend |
| MySQL | Banco de dados relacional |

- **Frontend:** parte visual da aplicação, responsável pelas interfaces e interações com o usuário.
- **Backend:** responsável pelas regras de negócio, processamento de informações e comunicação com o banco de dados.
- **Banco de dados:** responsável pelo armazenamento e gerenciamento das informações da aplicação.

## O que você vai aprender

Os projetos web do laboratório seguem, em sua maioria, uma arquitetura que separa o frontend do backend.

O Angular é utilizado para construir as interfaces, enquanto o Java com Spring Boot é responsável pelo processamento dos dados e pela disponibilização de APIs.

A comunicação entre essas partes normalmente ocorre por meio de requisições HTTP, utilizando APIs REST.

## 1. Angular — Desenvolvimento Frontend

O Angular é um framework utilizado para desenvolver aplicações web dinâmicas, organizadas em componentes reutilizáveis.

### Principais conceitos para aprender

| Conceito | O que aprender |
|---|---|
| TypeScript | Tipagem, classes, interfaces e funções |
| Componentes | Criação e reutilização de partes da interface |
| Templates | Utilização de HTML e associação com os componentes |
| Data Binding | Comunicação entre os dados e a interface |
| Serviços | Organização e compartilhamento de funcionalidades |
| Injeção de dependências | Utilização de serviços em componentes |
| Rotas | Navegação entre as páginas da aplicação |
| Formulários | Captura e validação de informações |
| HttpClient | Comunicação com as APIs do backend |

### Curso recomendado

**[Curso de Angular — Loiane Groner](https://loiane.training/cursos/angular)**

Curso introdutório que apresenta os principais fundamentos do Angular, desde a criação de componentes até serviços, formulários e comunicação HTTP.

> **Observação:** o curso utiliza versões mais antigas do Angular. Alguns comandos e estruturas podem ter mudado, mas os conceitos fundamentais continuam importantes. Durante o desenvolvimento, consulte também a [documentação oficial do Angular](https://angular.dev/).

## 2. Spring Boot — Desenvolvimento Backend

O Spring Boot é um framework Java que facilita a criação de aplicações web e APIs REST, organizando as responsabilidades do sistema em diferentes camadas.

### Principais conceitos para aprender

| Conceito | O que aprender |
|---|---|
| Java e POO | Classes, objetos, herança, interfaces e encapsulamento |
| Spring Boot | Estrutura e inicialização de um projeto |
| Maven | Gerenciamento de dependências e compilação |
| API REST | Comunicação entre sistemas por meio de HTTP |
| Controllers | Criação dos endpoints da aplicação |
| Services | Implementação das regras de negócio |
| Repositories | Comunicação com o banco de dados |
| Entities | Representação das tabelas do banco |
| JPA e Hibernate | Mapeamento e persistência dos dados |
| CRUD | Criação, leitura, atualização e exclusão de registros |
| DTOs | Transferência de dados entre as camadas |
| Injeção de dependências | Gerenciamento e utilização dos componentes do Spring |
| Tratamento de exceções | Gerenciamento de erros e respostas HTTP |
| Spring Security e JWT | Fundamentos de autenticação e autorização |

### Cursos recomendados

**[CRUD Angular + Spring — Loiane Groner](https://loiane.training/cursos/crud-angular-spring)**

Curso prático que demonstra a integração entre Angular e Spring Boot por meio do desenvolvimento de uma aplicação CRUD.

É especialmente recomendado para compreender como o frontend se comunica com o backend, como os dados são processados e como a aplicação interage com o banco de dados.

**[Tutorial complementar de Spring Boot — YouTube](https://www.youtube.com/watch?v=LXRU-Z36GEU)**

Material em vídeo para complementar o estudo e acompanhar exemplos práticos de desenvolvimento backend.

> **Observação:** alguns materiais utilizam versões antigas do Spring Boot e do Java. É importante compreender os conceitos ensinados, mas adaptar configurações, dependências e bibliotecas conforme as versões utilizadas nos projetos atuais do laboratório.

**Documentação de apoio:** [Spring Boot](https://docs.spring.io/spring-boot/index.html).

## 3. Integração entre Frontend e Backend

Após compreender os fundamentos de Angular e Spring Boot, é importante entender como essas tecnologias trabalham juntas.

### Conceitos essenciais

- **HTTP:** protocolo utilizado na comunicação entre frontend e backend.
- **GET, POST, PUT e DELETE:** métodos HTTP utilizados nas operações de uma API.
- **JSON:** formato utilizado para a troca de dados.
- **API REST:** conjunto de endpoints disponibilizados pelo backend.
- **Códigos de resposta HTTP:** identificação de sucesso ou falha em uma requisição, como 200, 201, 400, 404 e 500.
- **CORS:** configuração que controla o acesso às APIs por aplicações de outras origens.
- **Autenticação:** identificação do usuário que acessa a aplicação.
- **Autorização:** definição das funcionalidades que cada usuário pode acessar.

### Exemplo de funcionamento

1. O usuário preenche um formulário no Angular.
2. O Angular envia uma requisição HTTP para o backend.
3. O Controller do Spring Boot recebe a requisição.
4. O Service executa as regras de negócio.
5. O Repository consulta ou modifica os dados no banco.
6. O backend retorna uma resposta em JSON.
7. O Angular recebe a resposta e atualiza a interface.

## 4. Noções básicas de servidor e implantação

Além do desenvolvimento, é importante conhecer o funcionamento básico do ambiente em que as aplicações são hospedadas.

### Conceitos recomendados

| Conceito | O que aprender |
|---|---|
| Linux | Navegação por diretórios, arquivos, permissões e comandos básicos |
| SSH | Acesso remoto ao servidor |
| Git | Atualização do código a partir dos repositórios |
| Docker | Criação e execução de aplicações em containers |
| Docker Compose | Configuração e execução de múltiplos serviços |
| Portas | Comunicação e disponibilização dos serviços |
| Apache e Proxy Reverso | Encaminhamento das requisições para as aplicações |
| Logs | Identificação de erros e acompanhamento dos serviços |
| Variáveis de ambiente | Configuração das aplicações sem fixar dados sensíveis no código |

Não é necessário dominar toda a administração do servidor inicialmente. O objetivo é compreender como uma aplicação desenvolvida localmente pode ser executada e disponibilizada no ambiente do laboratório.

## 5. Prática recomendada

Após estudar os cursos, desenvolva uma aplicação CRUD simples utilizando Angular e Spring Boot.

A aplicação pode ser um pequeno cadastro de tarefas, produtos ou usuários, com as seguintes funcionalidades:

1. Listar registros cadastrados.
2. Adicionar um novo registro.
3. Editar um registro existente.
4. Excluir um registro.
5. Armazenar as informações em um banco de dados.

Durante o desenvolvimento, procure organizar o frontend em componentes e serviços e o backend em Controllers, Services, Repositories e Entities.

## 6. Ordem sugerida de estudos

1. **Fundamentos:** HTML, CSS, JavaScript, TypeScript, Java e orientação a objetos.
2. **Angular:** realizar o curso introdutório da Loiane, dando atenção especial a componentes, serviços, rotas e HTTP.
3. **Spring Boot:** estudar a criação de APIs REST e a organização das camadas do backend.
4. **Integração:** realizar o curso CRUD Angular + Spring da Loiane.
5. **Banco de dados:** compreender consultas SQL e o funcionamento do JPA/Hibernate.
6. **Servidor:** aprender comandos básicos de Linux, Docker e o processo de implantação.

Não é necessário concluir todos os cursos antes de começar a praticar. O ideal é alternar os estudos com pequenos exercícios e consultar a documentação sempre que necessário.

## Resultado e critérios de conclusão

- [ ] Compreendi a diferença entre frontend e backend.
- [ ] Conheço os principais conceitos do Angular.
- [ ] Compreendo a organização de uma aplicação Spring Boot.
- [ ] Entendo como funciona a comunicação entre Angular e Spring Boot.
- [ ] Consegui executar uma aplicação com frontend e backend.
