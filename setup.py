#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

__author__ = 'Radek Janoštík, Tomáš Mikula, Tomáš Urbanec, Roman Vyjídáček'
__email__ = 'radek.janostik@upol.cz, mail@tomasmikula.cz, tomas.urbanec@upol.cz, r.vyjidacek@gmail.com'
__version__ = '0.1.1'
__license__ = 'MIT license'

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# Requirements for end-user
requirements = ['Click>=7.0', 'mat4py>=0.4.2', 'h5py>=2.10.0']

# Requirements for test
setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest>=3', ]

setup(
    author=__author__,
    author_email=__email__,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
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
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='convertme',
    name='convertme',
    packages=find_packages(include=['convertme', 'convertme.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={'docs': ['sphinx']},
    url='https://github.com/mikulatomas/convertme',
    version=__version__,
    zip_safe=False,
)
