VIRTUALENV = python -m venv
VENV := $(shell echo $${VIRTUAL_ENV-.venv})
PYTHON = $(VENV)/bin/python
INSTALL_STAMP = $(VENV)/.install.stamp

all: install

runserver: install
	$(PYTHON) manage.py runserver

makemigrations: install
	$(PYTHON) manage.py migrate

migrate: install
	$(PYTHON) manage.py migrate

fixtures: install
	$(PYTHON) manage.py dumpdata \
       --natural-foreign menu \
	   --format yaml \
       --natural-primary \
       --verbosity 3 \
       --output menu/fixtures/initial_data.yaml

install: $(INSTALL_STAMP)
$(INSTALL_STAMP): $(PYTHON) requirements.txt
	$(VENV)/bin/pip install -U pip
	$(VENV)/bin/pip install -Ur requirements.txt
	touch $(INSTALL_STAMP)

virtualenv: $(PYTHON)
$(PYTHON):
	$(VIRTUALENV) $(VENV)

