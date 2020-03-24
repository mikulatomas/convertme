"""Top-level package for ConvertMe."""

from .dataset import Dataset
from .reader_interface import ReaderInterface
from .writer_interface import WriterInterface
from .csv.csv_reader import CsvReader
from .csv.csv_writer import CsvWriter
from .burmeister.burmeister_reader import BurmeisterReader
from .burmeister.burmeister_writer import BurmeisterWriter

__author__ = """Tomáš Mikula"""
__email__ = 'mail@tomasmikula.cz'
__version__ = '0.1.0'
