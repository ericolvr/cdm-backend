#!/bin/bash

echo "Start Migration  ..... ..... ..... ..... ....."
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
echo "End Migration ..... ..... ..... ..... ....."
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:9999 app.app.main