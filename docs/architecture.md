# Enterprise EMS Architecture


## Architecture Style

Modular Layered Architecture


Flow:


Router Layer

↓

Service Layer

↓

Repository Layer

↓

Database


## Layers


### Router

Handles:
- API endpoints
- Request validation
- Response


### Service

Handles:
- Business logic
- Validation
- Transactions


### Repository

Handles:
- Database operations


### Models

SQLAlchemy database entities


### Schemas

Pydantic request and response models


## Security Architecture

JWT
|
Refresh Token
|
RBAC
|
Permission Validation


## Database

MySQL database managed using Alembic migrations.