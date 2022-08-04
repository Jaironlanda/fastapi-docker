## Ahh yis magic

Fastapi + Postgresql + Pgadmin + Docker + asyncpg + alembic

## Setup

#### Docker
```bash
docker compose up
```

#### Create DB with alembic
```bash
docker exec -w /app/app api-server alembic upgrade head
```

### OR

#### Generate table with alembic
```bash
docker exec -w /app/app api-server alembic revision --autogenerate -m "Init"
```
### Ref

- https://testdriven.io/blog/fastapi-sqlmodel/
- https://sqlmodel.tiangolo.com/ 
