#!/bin/bash

echo "Building Docker image..."

docker compose build

echo "Starting containers..."

docker compose up -d

echo "Running Alembic migrations..."

docker compose exec app alembic upgrade head

echo "Deployment completed."