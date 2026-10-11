# FastAPI Auth Service

Serviço de autenticação para APIs, desenvolvido com FastAPI. Fornece registro de usuários, login com JWT, hash seguro de senha e persistência em PostgreSQL, com Redis e Docker para desenvolvimento local.

**Stack:** Python · FastAPI · PostgreSQL · SQLAlchemy · Alembic · Redis · Docker

---

## Funcionalidades

- Registro de usuários
- Login com JWT bearer token
- Hash seguro de senha com Passlib e Bcrypt
- Persistência de usuários em PostgreSQL
- Redis para recursos de cache ou sessão
- Migrations versionadas com Alembic
- Configuração por variáveis de ambiente
- Documentação automática com Swagger e ReDoc

---

## Arquitetura

```text
Client
  │
  ▼
Routers             # endpoints FastAPI
  │
  ▼
Services            # regras de negócio
  │
  ▼
Repositories        # acesso a dados
  │
  ▼
Models              # SQLAlchemy ORM
  │
  ▼
PostgreSQL / Redis
```

```text
app/
├── core/           # configuração, segurança e banco
├── models/         # entidades SQLAlchemy
├── repositories/   # consultas e persistência
├── routers/        # endpoints
├── schemas/        # contratos de entrada e saída
└── services/       # regras de negócio
alembic/            # migrations
```

---

## Como executar

### Pré-requisitos

- Python 3.10 ou superior
- Docker e Docker Compose, recomendados para PostgreSQL e Redis

### 1. Clonar

```bash
git clone [https://github.com/HighOffGrid/fastapi-auth-service.git](https://github.com/HighOffGrid/fastapi-auth-service.git)
cd fastapi-auth-service
```

### 2. Configurar ambiente

Crie seu arquivo local a partir do modelo:

```bash
cp .env.example .env
```

No PowerShell do Windows:

```powershell
Copy-Item .env.example .env
```

Edite o `.env` se necessário. Ele não deve ser enviado ao GitHub.

### 3. Rodar com Docker

```bash
docker compose up --build
```

### 4. Aplicar migrations

Em outro terminal:

```bash
alembic upgrade head
```

### 5. Acessar a documentação

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Executar sem Docker

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS

pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

---

## Autenticação

O serviço retorna um token JWT após login. Nas rotas protegidas, envie o token no cabeçalho:

```http
Authorization: Bearer <jwt>
```

A lista completa de endpoints e modelos de request/response está disponível no Swagger em `/docs`.

---

## Segurança

- Hash de senha com Bcrypt
- Tokens JWT com expiração configurável
- Segredos configurados por variáveis de ambiente
- Models e schemas separados para evitar expor campos sensíveis pela API

---

## Próximos passos

- Adicionar testes automatizados com Pytest
- Criar pipeline de CI com GitHub Actions
- Implementar rate limiting no login
- Revisar fluxos contra o OWASP API Security Top 10
