#!/usr/bin/env python

"""Setup for trim."""

from __future__ import unicode_literals

import ast
from distutils import core


def version():
    """Return version string."""
    with open('trim') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s


with open('README.rst') as readme:
    core.setup(name='trim',
               version=version(),
               description='Trims trailing whitespace from files.',
               long_description=readme.read(),
               license='Expat License',
               author='Steven Myint',
               url='https://github.com/myint/trim',
               classifiers=[
                   'Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Environment :: Console',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'License :: OSI Approved :: MIT License'],
               keywords='trim, strip, format, trailing, whitespace',
               scripts=['trim'])
