#!/usr/bin/env python

"""The setup script."""

import pathlib
from setuptools import setup, find_packages

__author__ = "Radek Janoštík, Tomáš Mikula, Tomáš Urbanec, Roman Vyjídáček"
__email__ = "radek.janostik@upol.cz, mail@tomasmikula.cz, tomas.urbanec@upol.cz, r.vyjidacek@gmail.com"
__version__ = "0.1.4"
__license__ = "MIT license"


setup(
    name="convertme",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="Simple dataset convertor in Python",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "convertme=convertme.cli:main",
        ],
    },
    install_requires=["Click>=7.0", "mat4py>=0.4.3", "h5py>=2.10.0", "bitarray>=1.2.1"],
    license=__license__,
    long_description=pathlib.Path("README.rst").read_text()
    + "\n\n"
    + pathlib.Path("HISTORY.rst").read_text(),
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="convertme",
    packages=find_packages(include=["convertme", "convertme.*"]),
    extras_require={"test": ["pytest", "pytest-cov"], "docs": ["sphinx"]},
    url="https://github.com/mikulatomas/convertme",
    zip_safe=False,
)
