PYTHON_GLOBAL = python
VENV = venv/bin/
PYTHON = $(VENV)python
PIP = $(VENV)pip
GIT = git

.PHONY: install run build-requirements install-requirements requirements

install:
	$(info Creating virtual environment...)
	@$(PYTHON_GLOBAL) -m venv venv
	$(info Upgrading pip...)
	@$(PIP) install --upgrade pip
	$(info Installing requirements...)
	@$(PIP) install -r requirements.txt
	$(info copying .env.example to .env)
	@cp .env.sample .env

serve:
	@$(PYTHON) main.py

build-requirements:
	$(info Building requirements...)
	@$(PIP)-compile requirements.in -o requirements.txt

install-requirements:
	$(info Installing requirements...)
	@$(PIP)-sync requirements.txt

requirements: build-requirements install-requirements
	$(info Requirements updated and installed)
