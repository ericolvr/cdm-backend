#!/bin/bash

echo "Iniciou a migração ..... ..... ..... ..... ....."
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
echo "Finalizou a migração ..... ..... ..... ..... ....."
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:9999 app.main:app