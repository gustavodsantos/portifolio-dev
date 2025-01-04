# Portfólio Dev

Bem-vindo ao repositório do **Portfólio Dev**, um projeto desenvolvido para apresentar as habilidades em desenvolvimento web utilizando o framework **Django**.
Este projeto é um site dinâmico com funcionalidades básicas para apresentação de informações, organização de cursos e gerenciamento de conteúdo.

> **Dica**: Você também pode acessar o projeto na instância configurada do EC2. Use o link abaixo:
   [Projeto ao vivo](http://ec2-54-167-236-164.compute-1.amazonaws.com)

## 📋 Requisitos

Certifique-se de ter os seguintes pré-requisitos instalados antes de iniciar:

- **Python 3.12 ou superior**
- **PostgreSQL 12 ou superior**
- **Docker e Docker Compose** (opcional, mas recomendado)

## 📂 Estrutura do Projeto

A estrutura principal do projeto está organizada da seguinte forma:

- **`backend/`**: Contém o core do projeto Django.
- **`docker/`**: Arquivos de configuração Docker para o ambiente de desenvolvimento.
- **`static/`**: Arquivos estáticos (CSS, imagens, etc).
- **`templates/`**: Templates HTML para renderização das páginas.
- **`pytest/`**: Testes automatizados com cobertura de código.

## 🚀 Como executar o projeto

### 1. Configurar variáveis de ambiente
Crie um arquivo `.env` na pasta `backend` baseado no arquivo `env-sample`.

### 2. Rodando com Docker
Para acelerar o setup, é possível usar o **Docker Compose** para configurar o ambiente com PostgreSQL e Django:

```bash
docker-compose up --build
```

Isso irá criar três serviços:
- **`database`**: Serviço PostgreSQL
- **`backend`**: Aplicação Django
- **`nginx`**: Servidor Web para servir os recursos estáticos.

Após o build, a aplicação estará acessível em **http://localhost**.

### 3. Rodando sem Docker
- Instale o [Poetry](https://python-poetry.org/) para gerenciar as dependências:
  ```bash
  pip install poetry
  ```
- Instale as dependências:
  ```bash
  poetry install
  ```
- Execute as migrações e inicie o servidor de desenvolvimento:
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

Após esses passos, o site estará disponível em **http://127.0.0.1:8000**.

## 📦 Tecnologias Utilizadas

- **Django 5.0**: Framework principal para o backend.
- **PostgreSQL**: Banco de dados relacional.
- **Docker**: Criação de contêineres para o ambiente de desenvolvimento.
- **Gunicorn**: Servidor WSGI de produção para Django.
- **Nginx**: Proxy reverso e servidor de arquivos estáticos.
- **Bootstrap 5.3**: Estilização responsiva do frontend.

## 🛠️ Funcionalidades do Projeto

- **Página Inicial**: Uma página com introdução e links para navegação do site.
- **Apresentação Pessoal**: Uma seção destacando informações sobre o desenvolvedor.
- **Gestão de Cursos**:
  - Listagem de cursos disponíveis.
  - Detalhes de cada curso.
- **Administração**:
  - Gerenciamento de cursos pela interface do Django Admin.

## 🧪 Testes

Os testes automatizados foram implementados utilizando o **pytest**. Para executá-los:

```bash
poetry run pytest
```

O relatório de cobertura de código será gerado após a execução.

## 🔒 Segurança

**AVISO**: Não use `DEBUG=True` em produção. Garanta a configuração adequada de variáveis sensíveis no ambiente.

## 🤝 Contribuições

Sinta-se à vontade para contribuir com o projeto. Para isso:

1. **Faça o fork do repositório**;
2. **Crie uma nova branch**:
    ```bash
    git checkout -b minha-feature
    ```
3. Envie suas alterações:
    ```bash
    git push origin minha-feature
    ```
4. Abra um **Pull Request**.

## 📬 Contato

- **Desenvolvedor**: [Gustavo Junior dos Santos](https://www.linkedin.com/in/gustavo-junior-dos-santos/)
- **GitHub**: [github.com/gustavodsantos](https://github.com/gustavodsantos)

## 📝 Licença

Este projeto está licenciado sob os termos da licença **MIT**. Sinta-se livre para utilizá-lo conforme descrito nos termos da licença.

---
Site criado por [Gustavo Junior dos Santos](https://www.linkedin.com/in/gustavo-junior-dos-santos/).