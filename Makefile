create-venv:
	python3 -m venv venv

install:
	pip3 install -r requirements.txt

populate:
	python manage.py populate_db

start-app:
	FLASK_ENV=development python3 manage.py run

run-tests:
	python3 manage.py test

run-coverage:
	python3 -m pytest -v --cov=app --cov-report=term-missing > coverage.txt

run-formater:
	autopep8 --max-line-length 110 --experimental -i -r app/

run-lint:
	autoflake --remove-all-unused-imports --remove-unused-variables --recursive --in-place . --exclude=__init__.py,venv,conftest.py,manage.py
	flake8 app/
	isort app/	
