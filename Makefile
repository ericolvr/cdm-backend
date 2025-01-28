# ANSI color codes
COLOR_RESET=\033[0m
COLOR_BOLD=\033[1m
COLOR_GREEN=\033[32m
COLOR_YELLOW=\033[33m

help:
	@echo ""
	@echo "  $(COLOR_YELLOW)Available targets:$(COLOR_RESET)"
	@echo ""
	@echo "  $(COLOR_GREEN)upgrade-pip$(COLOR_RESET)		- Upgrade Pip Version"
	@echo "  $(COLOR_GREEN)install$(COLOR_RESET)		- Install Libraries / Dependencies"
	@echo "  $(COLOR_GREEN)freeze$(COLOR_RESET)		- Freeze Libraries / Dependencies"
	@echo "  $(COLOR_GREEN)start$(COLOR_RESET)		- Start MySQL Database"
	@echo "  $(COLOR_GREEN)migrations$(COLOR_RESET)		- Start Alembic"
	@echo "  $(COLOR_GREEN)migrate$(COLOR_RESET)		- Upgrade Alembic Head"
	@echo "  $(COLOR_GREEN)run$(COLOR_RESET)			- Run FastAPI"
	@echo ""
	@echo "  $(COLOR_YELLOW)Note:$(COLOR_RESET) Use 'make <target>' to execute a specific target."
	@echo ""

upgrade-pip:
	pip install --upgrade pip

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt
	
start:
	docker compose up -d

migrations:
	alembic revision --autogenerate -m "Initial migration"
	
migrate:
	alembic upgrade head


run:
	uvicorn app.main:app --reload --host 127.0.0.1  --port 9999
.PHONY: help, upgrade-pip, install, freeze, migrations, migrate, run