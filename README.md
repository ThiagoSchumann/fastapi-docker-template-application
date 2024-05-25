[Leia em Português](README.pt-br.md)

### FastAPI-Docker-Base

A template API project using Docker, FastAPI, SQLModel, and PostgreSQL.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-2496ED?style=flat&logo=sqlalchemy&logoColor=white)

## Description

This project is a template for creating robust and scalable APIs with FastAPI, utilizing Docker for containerization and PostgreSQL as the database.

## Setup

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ThiagoSchumann/FastAPI-Docker-Base
   cd FastAPI-Docker-Base
   ```

2. Start Docker containers:
   ```bash
   docker-compose up -d --build
   ```

## Usage

### Important Commands

#### Reset Project

1. Remove migration files:
   ```bash
   rm backend/migrations/versions/*.py
   ```

2. Take down existing containers and volumes:
   ```bash
   docker-compose down -v
   ```

3. Rebuild and start containers in detached mode:
   ```bash
   docker-compose up -d --build
   ```

4. Generate a new Alembic migration file:
   ```bash
   docker-compose exec web alembic revision --autogenerate -m "init"
   ```

5. Include changes in the new migration file:
   ```bash
   import sqlmodel
   ```

6. Apply the latest Alembic migrations:
   ```bash
   docker-compose exec web alembic upgrade head
   ```

7. Check container logs:
   ```bash
   docker-compose logs web
   ```

### Testing

To test the application, run:
```bash
docker-compose down -v
docker-compose up -d --build
docker-compose logs web
```

Check tables in psql:
```bash
docker-compose exec db psql --username=postgres --dbname=foo
\dt
\q
```

## Project Structure

```plaintext
.
├── backend
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

- **backend/app**: Main application files (entry point, data models, database configuration, and CRUD operations).
- **backend/tests**: Automated tests.
- **backend/migrations**: Alembic migrations.
- **docker-compose.yml**: Docker Compose configuration.
- **Dockerfile**: Docker configuration.

## License

This project is licensed under the terms of the [MIT License](LICENSE).

## Author

Developed by [Thiago Schumann](https://github.com/ThiagoSchumann).

## Contact

For more information, contact:
- [![Email](https://img.shields.io/badge/Email-thiagoarturschumann@gmail.com-red?style=flat&logo=gmail&logoColor=white)](maito:thiagoarturschumann@gmail.com)
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-thiagoschumann-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thiagoschumann/)
