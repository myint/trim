check:
	pep8 trim.py setup.py
	pep257 trim.py setup.py
	pylint --report=no --include-ids=yes --disable=C0103 --rcfile=/dev/null trim.py setup.py
	python setup.py --long-description | rst2html --strict > /dev/null
	scspell trim.py setup.py test_trim.py README.rst

readme:
	@restview --long-description

register:
	@python setup.py register sdist upload
	@srm ~/.pypirc
