.ONESHELL:
.DELETE_ON_ERROR:

SHELL := /bin/bash

.PHONY: activate requirements build run trunk app

build:
	cd ../.. && \
	docker build -f ./app/Dockerfile -t vae .

run: build
	cd ../.. && \
	docker run --env-file ./app/.integration.env --rm -it --name vae -p 8000:8000 vae

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


trunk:
	trunk check ./ && \
    trunk fmt ./