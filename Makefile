check:
	pycodestyle trim.py setup.py
	pydocstyle trim.py setup.py
	pylint \
		--reports=no \
		--rcfile=/dev/null \
		--disable=invalid-name \
		--disable=no-else-return \
		trim.py setup.py
	python setup.py --long-description | rstcheck -
	scspell trim.py setup.py test_trim.py README.rst

readme:
	@restview --long-description --strict
