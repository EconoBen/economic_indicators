.ONESHELL:
.DELETE_ON_ERROR:

SHELL := /bin/bash

.PHONY: activate requirements build run format app

build:
	docker build -f ./Dockerfile -t economic_indicators .

run: build
	docker run --env-file ./app/.env --rm -it --name economic_indicators -p 8501:8501 economic_indicators

app:
	poetry run streamlit run app/main.py

activate:
	@echo "Connecting pyenv & poetry..."
	poetry config virtualenvs.in-project true && \
	poetry env use $$(pyenv which python) && \
	poetry config virtualenvs.prefer-active-python true
	
	@echo "Done!"

requirements:
	poetry export -f requirements.txt --without-hashes | cut -f1 -d\; > requirements.txt


format:
	poetry run isort . && \
	poetry run black ./ && \
	poetry run flake8 ./ 
	
