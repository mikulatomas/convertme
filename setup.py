#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from convertme import __author__, __email__, __version__, __license__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author=__author__,
    author_email=__email__,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Simple dataset convertor in Python",
    entry_points={
        'console_scripts': [
            'convertme=convertme.cli:main',
        ],
    },
    install_requires=requirements,
    license=__license__,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='convertme',
    name='convertme',
    packages=find_packages(include=['convertme', 'convertme.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mikulatomas/convertme',
    version=__version__,
    zip_safe=False,
)
