# FastAPI Auth Service

Serviço de autenticação desenvolvido com FastAPI, utilizando JWT, PostgreSQL e Redis.

Projeto criado para estudo de autenticação e arquitetura backend moderna.

---

Tecnologias:
-	FastAPI
-	PostgreSQL
-	SQLAlchemy
-	Redis
-	Docker
-	Alembic (database migrations)
-	Passlib / Bcrypt (hash de senha)
-	Python-Jose (JWT)
-	Pydantic
-	Python-dotenv
-	Uvicorn

---

Funcionalidades:
-	Registro de usuário
-	Login com JWT
-	Hash seguro de senha
-	Persistência em PostgreSQL
-	Cache com Redis
-	Migrations com Alembic
-	Configuração via variáveis de ambiente

---

## Arquitetura

Client
   │
   ▼
Routers (FastAPI)
   │
   ▼
Services (Regras de negócio)
   │
   ▼
Repositories (Acesso ao banco)
   │
   ▼
Models (SQLAlchemy ORM)
   │
   ▼
PostgreSQL / Redis

---

## Estrutura do projeto

```
app/
 ├── models
 ├── schemas
 ├── services
 ├── repositories
 ├── routers
 └── core
```

---

## Objetivo


Este projeto foi desenvolvido para praticar a implementação de autenticação em APIs utilizando FastAPI e boas práticas de desenvolvimento backend.

---

## Rodando o projeto


Clone o repositório:

```bash
git clone https://github.com/HighOffGrid/fastapi-auth-service
cd fastapi-auth-service
```
---

Instale as dependências:
```
pip install -r requirements.txt
```
---

## Rodando com Docker
```
docker compose up --build
```
---

## Executando a API

Para rodar sem Docker (apenas para desenvolvimento):
```
uvicorn app.main:app --reload

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
```
