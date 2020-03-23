"""Top-level package for ConvertMe."""

from .dataset import Dataset
from .reader_interface import ReaderInterface
from .writer_interface import WriterInterface
from .csv.csv_reader import CsvReader
from .csv.csv_writer import CsvWriter

__author__ = """Tomáš Mikula"""
__email__ = 'mail@tomasmikula.cz'
__version__ = '0.1.0'
