# Setup Guide


## Requirements

- Python 3.13+
- MySQL
- Redis


## Environment

Create .env file:


DATABASE_URL=

SECRET_KEY=

REDIS_HOST=

REDIS_PORT=


## Migration

Create migration:

alembic revision --autogenerate -m "message"


Apply migration:

alembic upgrade head


## Start Server

uvicorn main:app --reload