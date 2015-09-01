clean: clean-build clean-pyc

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

pep8:
	@flake8 --ignore=E402,F821 --exclude=migrations,south_migrations pinba

release: clean
	@python setup.py register sdist upload --sign
	@python setup.py bdist_wheel upload --sign

run-server:
	@cd demo && python manage.py runserver --traceback

run-shell:
	@cd demo && python manage.py shell

test:
	@cd demo && ./manage.py test pinba

coverage:
	@cd demo && \
	coverage run --branch --source=pinba ./manage.py test pinba && \
	coverage report --omit="*/pinba/test*,*/pinba/migrations/*,*/pinba/south_migrations*,*/pinba/admin*,*/pinba/management/*"
