### FastAPI-Docker-Base

Um projeto de template de API utilizando Docker, FastAPI, SQLModel e PostgreSQL.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-2496ED?style=flat&logo=sqlalchemy&logoColor=white)

## Descrição

Este projeto é um template para criar APIs robustas e escaláveis com FastAPI, utilizando Docker para contêinerização e PostgreSQL como banco de dados.

## Configuração

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/ThiagoSchumann/FastAPI-Docker-Base
   cd FastAPI-Docker-Base
   ```

2. Inicie os contêineres Docker:
   ```bash
   docker-compose up -d --build
   ```

## Uso

### Comandos Importantes

#### Resetar Projeto

1. Remova arquivos de migração:
   ```bash
   rm src/migrations/versions/*.py
   ```

2. Derrube os contêineres e volumes existentes:
   ```bash
   docker-compose down -v
   ```

3. Reconstrua e inicie os contêineres em modo destacado:
   ```bash
   docker-compose up -d --build
   ```

4. Gere um novo arquivo de migração Alembic:
   ```bash
   docker-compose exec web alembic revision --autogenerate -m "init"
   ```

5. Inclua as mudanças no novo arquivo de migração:
   ```bash
   import sqlmodel
   ```

6. Aplique as últimas migrações Alembic:
   ```bash
   docker-compose exec web alembic upgrade head
   ```

7. Verifique os logs do contêiner:
   ```bash
   docker-compose logs web
   ```

### Testes

Para testar a aplicação, execute:
```bash
docker-compose down -v
docker-compose up -d --build
docker-compose logs web
```

Verifique as tabelas no psql:
```bash
docker-compose exec db psql --username=postgres --dbname=foo
\dt
\q
```

## Estrutura do Projeto

```plaintext
.
├── src
│   ├── app
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── crud.py
│   │   └── ...
│   ├── tests
│   │   ├── test_main.py
│   │   └── ...
│   └── migrations
│       ├── versions
│       │   └── ...
│       └── env.py
├── docker-compose.yml
└── Dockerfile
```

- **src/app**: Arquivos principais da aplicação (ponto de entrada, modelos de dados, configuração do banco de dados e operações CRUD).
- **src/tests**: Testes automatizados.
- **src/migrations**: Migrações Alembic.
- **docker-compose.yml**: Configuração do Docker Compose.
- **Dockerfile**: Configuração do Docker.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

## Autor

Desenvolvido por [Thiago Schumann](https://github.com/ThiagoSchumann).

## Contato

Para mais informações, entre em contato:
- [![Email](https://img.shields.io/badge/Email-thiagoarturschumann@gmail.com-red?style=flat&logo=gmail&logoColor=white)](mailto:thiagoarturschumann@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-thiagoschumann-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thiagoschumann/)