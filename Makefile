check:
	pep8 trim.py setup.py
	pep257 trim.py setup.py
	pylint --report=no --include-ids=yes --disable=C0103,F0401,R0914,E1101 --rcfile=/dev/null trim.py setup.py
	python setup.py --long-description | rst2html --strict > /dev/null
	scspell trim.py setup.py test_trim.py README.rst

readme:
	@python setup.py --long-description | rst2html --strict > README.html
	@python -m webbrowser -n "file://${PWD}/README.html"

register:
	@python setup.py register
	@python setup.py sdist upload
	@srm ~/.pypirc
