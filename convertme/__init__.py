"""Top-level package for ConvertMe."""

from .dataset import Dataset
from .reader_interface import ReaderInterface
from .writer_interface import WriterInterface
from .csv.csv_reader import CsvReader
from .csv.csv_writer import CsvWriter
from .burmeister.burmeister_reader import BurmeisterReader
from .burmeister.burmeister_writer import BurmeisterWriter

__author__ = 'Radek Janoštík, Tomáš Mikula, Roman Vyjídáček'
__email__ = 'radek.janostik@upol.cz, mail@tomasmikula.cz, r.vyjidacek@gmail.com'
__version__ = '0.1.0'
__license__ = 'MIT license'
