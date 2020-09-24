default: help

PYTHON_VERSION=3.8
VENV_DIR=venv

.PHONY: install-dev-venv
install-dev-venv: ## Install a dev environment (locally).
	python$(PYTHON_VERSION) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install pip-tools
	$(VENV_DIR)/bin/pip-sync requirements.txt dev-requirements.txt

.PHONY: install-prod-venv-alwaysdata
install-prod-venv-alwaysdata: ## Install prod environment at alwaysdata.
	PYTHON_VERSION=$(PYTHON_VERSION) python -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install pip-tools
	$(VENV_DIR)/bin/pip-sync requirements.txt prod-requirements.txt

.PHONY: update-dev-venv
update-dev-venv: ## Update dev environment.
	$(VENV_DIR)/bin/pip-compile --upgrade
	$(VENV_DIR)/bin/pip-compile --upgrade dev-requirements.in
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip-sync requirements.txt dev-requirements.txt

.PHONY: update-prod-venv
update-prod-venv: ## Update prod environment.
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip-compile --upgrade prod-requirements.in
	$(VENV_DIR)/bin/pip-sync requirements.txt prod-requirements.txt

.PHONY: create-dev-venv
create-dev-venv: ## Create a dev environment.
	python$(PYTHON_VERSION) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install pip-tools
	$(VENV_DIR)/bin/pip-compile
	$(VENV_DIR)/bin/pip-compile prod-requirements.in
	$(VENV_DIR)/bin/pip-compile dev-requirements.in
	$(VENV_DIR)/bin/pip-sync requirements.txt dev-requirements.txt

.PHONY: migrations
migrations: ## Create new migrations.
	$(VENV_DIR)/bin/python manage.py makemigrations

.PHONY: migrate
migrate: ## Apply migrations.
	$(VENV_DIR)/bin/python manage.py migrate

.PHONY: collectstatic
collectstatic: ## Collect static files.
	mkdir -p site_media/media
	mkdir -p site_media/static
	$(VENV_DIR)/bin/python manage.py collectstatic

.PHONY: install-django
install-django: migrate ## Run some Django initialization commands.
	$(VENV_DIR)/bin/python manage.py populate_db
	$(VENV_DIR)/bin/python manage.py createsuperuser

.PHONY: clean-static
clean-static: ## Remove collected static files.
	rm -rf site_media

.PHONY: clean-migrations
clean-migrations: ## Remove all Django migrations and database.
	find . -path "*/migrations/*.py" -not -path "./$(VENV_DIR)*" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -not -path "./$(VENV_DIR)*" -delete
	rm -f db.sqlite3

.PHONY: clean-python
clean-python: ## Clean Django environment.
	find . -path "*.pyc" -not -path "./$(VENV_DIR)*" -delete
	find . -path "*/__pycache__" -not -path "./$(VENV_DIR)*" -delete

.PHONY: reinstall-django
reinstall-django: clean-static clean-migrations clean-python migrations install-django ## Reinstall a fresh Django environment.

.PHONY: install-dev-front
install-dev-front: ## Install a dev front-end environment (locally).
	npm install

.PHONY: clean-front
clean-front: ## Clean front-end environment.
	rm -rf elm-stuff
	rm -rf node_modules
	rm -f package-lock.json

.PHONY: watch
watch: ## Turn on webpack watch mode.
	npm run watch

.PHONY: build
build: ## Build the front-end bundle in production mode.
	npm run build

.PHONY: serve
serve: ## Starts a lightweight development Web server on the local machine.
	$(VENV_DIR)/bin/python manage.py runserver 127.0.0.1:8000

.PHONY: quickstart
quickstart: install-dev-venv migrate install-django serve ## Quicktart demo app.

.PHONY: install-dev
install-dev: install-dev-front install-dev-venv install-django ## Install development environment.

.PHONY: generate_secret_key
generate_secret_key: ## Generates a secret key for production.
	@$(VENV_DIR)/bin/python utils/secret_key.py

.PHONY: help
help: ## Lists all the available commands.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
