# Makefile
.PHONY: install update format lint test sec build upload-pypi upload-pypitest export

install:
	@poetry run python -m pip install --upgrade pip
	@poetry run pip install -U pip setuptools
	@poetry install
	@poetry run pip install -U .
update:
	@poetry update	
format:
	@poetry run darker .
lint:
	@poetry run darker --check .
	@poetry run darker --isort .
test:
	@poetry run pytest -v
sec:
	@poetry run pip-audit
build:
	@poetry run python setup.py sdist bdist_wheel
upload-pypi:
	@poetry run python -m twine upload dist/*
upload-pypitest:
	@poetry run python -m twine upload --verbose --repository testpypi dist/*
export:
	@poetry export -f requirements.txt --without-hashes  > requirements.txt
	@poetry export --dev -f  requirements.txt --without-hashes  > requirements-dev.txt
