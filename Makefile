# Makefile
.PHONY: install update format lint test sec

install:
	@poetry run python -m pip install --upgrade pip
	@poetry run pip install -U pip setuptools
	@poetry install
	@poetry run pip install -U .
update:
	@poetry update	
format:
	@poetry run blue .
	@poetry run isort .
	@poetry run pydocstyle .
lint:
	@poetry run darker --check --isort .
test:
	@poetry run pytest -v
sec:
	@poetry run pip-audit
