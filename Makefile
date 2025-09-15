.PHONY: help install install-dev test lint check tidy version-dev version-release clean
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	uv sync

install-dev: ## Install development dependencies
	uv sync --all-extras

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=python_project_init --cov-report=html --cov-report=term

lint: ## Run linters
	uv run ruff check python_project_init tests
	uv run pyright python_project_init

tidy: ## Fix formatting and linting issues
	uv run ruff format python_project_init tests
	uv run ruff check --fix python_project_init tests
	uv run black python_project_init tests

check: lint ## Run all checks (alias for lint)

version-dev: ## Bump development version
	@current_version=$$(grep -E "^__version__ = " python_project_init/__init__.py | cut -d '"' -f2); \
	if [[ $$current_version =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)$$ ]]; then \
		major=$${BASH_REMATCH[1]}; \
		minor=$${BASH_REMATCH[2]}; \
		patch=$${BASH_REMATCH[3]}; \
		new_patch=$$((patch + 1)); \
		new_version="$$major.$$minor.$$new_patch"; \
		sed -i '' 's/__version__ = ".*"/__version__ = "'$$new_version'"/' python_project_init/__init__.py; \
		echo "Version bumped to $$new_version"; \
	else \
		echo "Could not parse current version: $$current_version"; \
		exit 1; \
	fi

version-release: ## Bump minor version for release
	@current_version=$$(grep -E "^__version__ = " python_project_init/__init__.py | cut -d '"' -f2); \
	if [[ $$current_version =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)$$ ]]; then \
		major=$${BASH_REMATCH[1]}; \
		minor=$${BASH_REMATCH[2]}; \
		new_minor=$$((minor + 1)); \
		new_version="$$major.$$new_minor.0"; \
		sed -i '' 's/__version__ = ".*"/__version__ = "'$$new_version'"/' python_project_init/__init__.py; \
		echo "Version bumped to $$new_version"; \
	else \
		echo "Could not parse current version: $$current_version"; \
		exit 1; \
	fi

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build: ## Build Docker image
	docker build -t python-project-init:latest .

docker-run: ## Run Docker container
	docker run --rm -it python-project-init:latest