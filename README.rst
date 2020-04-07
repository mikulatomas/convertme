===========================
ConvertMe -- Ayoyoyo Wololo
===========================


.. image:: https://img.shields.io/pypi/v/convertme
        :target: https://pypi.python.org/pypi/convertme

.. image:: https://img.shields.io/github/license/mikulatomas/convertme
        :target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/travis/mikulatomas/convertme.svg
        :target: https://travis-ci.org/mikulatomas/convertme.svg?branch=master

.. image:: https://codecov.io/gh/mikulatomas/convertme/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/mikulatomas/convertme


Simple dataset convertor in Python. Currently memory hungry in case of large datasets.

.. image:: https://img.youtube.com/vi/Up2eawxvTmg/0.jpg
  :target: https://www.youtube.com/watch?v=Up2eawxvTmg

.. * Documentation: https://convertme.readthedocs.io.


Installation
------------
Install package via ``pip``:

.. code:: bash

        $ pip install convertme

Use the provided CLI:

.. code::

        $ convertme --help
        Usage: convertme [OPTIONS]

        Options:
        -if, --input-format [csv|fimi|cxt|mat|cex]
                                        [required]
        -of, --output-format [csv|fimi|cxt|mat|cex]
                                        [required]
        -i, --input TEXT                Input file, skip it for stdin.
        -o, --output TEXT               Output file, skip it for stdout.
        --input-delimiter TEXT          (CSV) Delimiter of input.  [default: ,]
        --output-delimiter TEXT         (CSV) Delimiter of output.  [default: ,]
        --objects-col INTEGER           (CSV) Index of column with object labels,
                                        typically 0, ignored on default.

        --attributes-row INTEGER        (CSV) Index of row with attribute labels,
                                        typically 0, ignored on default.

        --true-values TEXT              (CSV) Values which will be count as True,
                                        comma separated.

        --help                          Show this message and exit.

Basic usage:
------------
Convert simple ``csv`` file to ``fimi`` format:

.. code:: bash

        $ convertme -i dataset.csv -if=csv -o dataset.fimi -of=fimi

Content of ``dataset.csv``:

.. code:: 

        1,0,1,0
        0,1,0,1

Content of ``dataset.fimi``:

.. code:: 

        0 2
        1 3

Supported formats
-----------------
* csv
* burmeister (.cxt)
* fimi
* matlab (version<=7.3)
* conexp (.cex)

Development
-----------
Clone this repository to the folder, then:

.. code:: bash

        # create virtualenv (optional)
        $ mkvirtualenv convertme -p python3

        #if is not actived (optional)
        $ workon convertme 

        $ pip install -e .

        $ python setup.py test
  
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
