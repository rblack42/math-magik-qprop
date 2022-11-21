.PHONY: venv
venv:	## Create Python virtual environment
	test -d .venv || \
	python -m venv .venv

.PHONY: init
init:  ## update pip and install pip-tools
	pip install -U pip
	pip install pip-tools

.PHONY: reqs
reqs: requirements.in 	## Load Python requirements
	pip-compile --resolver=backtracking
	pip install -r requirements.txt

.PHONY: test
test: ## Run unit tests
	python -m pytest

.PHONY: changes
changes:	## create CHANGES file from git logs
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

.PHONY: dev
dev:		## Install package in development mode
	python -m pip install --editable .

.PHONY: run
run:
	python -m mmqprop

