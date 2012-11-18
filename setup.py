#!/usr/bin/env python
"""Setup for trim."""

from distutils import core


def version():
    """Return version string."""
    with open('trim') as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                import ast
                return ast.literal_eval(line.split('=')[1].strip())


with open('README.rst') as readme:
    core.setup(name='trim',
               version=version(),
               description='Trims trailing whitespace from files.',
               long_description=readme.read(),
               license='Expat License',
               author='myint',
               url='https://github.com/myint/trim',
               classifiers=['Intended Audience :: Developers',
                            'Environment :: Console',
                            'Programming Language :: Python :: 2',
                            'Programming Language :: Python :: 3',
                            'License :: OSI Approved :: MIT License'],
               keywords='trim, format, trailing, whitespace',
               scripts=['trim'])
