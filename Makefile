#!make
SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -euc
MAKEFLAGS += --warn-unexport defined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: install lint format test cov cov-htmlbuild clean

install:
	@poetry lock --no-update
	@poetry install

lint:
	@poetry run black --check .
	@poetry run isort -s .cache/ -s dist/ -s .venv/ -c . --profile black
	@poetry run flake8
	@poetry run mypy .

format:
	@poetry run black .
	@poetry run isort -s .cache/ -s dist/ -s .venv/ . --profile black

test:
	@poetry run pytest --no-header -v

cov:
	@poetry run pytest --no-header -v --cov . --cov-branch

cov-html:
	@poetry run pytest --no-header -v --cov . --cov-branch --cov-report html

build:
	@poetry build

clean:
	@rm -rf dist/
