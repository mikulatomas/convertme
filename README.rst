=========
ConvertMe
=========


.. .. image:: https://img.shields.io/pypi/v/convertme.svg
..         :target: https://pypi.python.org/pypi/convertme

.. image:: https://img.shields.io/travis/mikulatomas/convertme.svg
        :target: https://travis-ci.org/mikulatomas/convertme.svg?branch=development

.. image:: https://codecov.io/gh/mikulatomas/convertme/branch/development/graph/badge.svg
  :target: https://codecov.io/gh/mikulatomas/convertme

.. .. image:: https://readthedocs.org/projects/convertme/badge/?version=latest
..         :target: https://convertme.readthedocs.io/en/latest/?badge=latest
..         :alt: Documentation Status


Simple dataset convertor in Python. Not released on PyPy yet.

* Free software: MIT license
.. * Documentation: https://convertme.readthedocs.io.

Development
------------
Clone this repo to the folder, then:

.. code:: bash

        mkvirtualenv convertme -p python3

        workon convertme #if is not actived

        pip install -e .

        pip install -r requirements_dev.txt

Supported formats
--------

* csv
* burmeister

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
