import pytest
from convertme import CsvReader


def test_csv_reader(tmp_path):
    CONTENT = """1;0;1;0"""

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader()
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == ['0']
    assert dataset.attributes == list(map(str, range(4)))


def test_csv_reader_external_objects_attributes(tmp_path):
    CONTENT = """1;0;1;0"""
    OBJECTS = ['0']
    ATTRIBUTES = ['a', 'b', 'c', 'd']

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader(objects=OBJECTS, attributes=ATTRIBUTES)
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == OBJECTS
    assert dataset.attributes == ATTRIBUTES


def test_csv_reader_internal_objects_attributes(tmp_path):
    CONTENT = """id;a;b;c;d
0;1;0;1;0
"""

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader(objects_col=0, attributes_row=0)
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == ['0']
    assert dataset.attributes == ['a', 'b', 'c', 'd']


def test_csv_reader_internal_attributes(tmp_path):
    CONTENT = """id;a;b;c;d
1;0;1;0
"""

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader(attributes_row=0)
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == ['0']
    assert dataset.attributes == ['a', 'b', 'c', 'd']


def test_csv_reader_internal_attributes2(tmp_path):
    CONTENT = """1;0;1;0
id;a;b;c;d
"""

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader(attributes_row=1)
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == ['0']
    assert dataset.attributes == ['a', 'b', 'c', 'd']


def test_csv_reader_internal_objects(tmp_path):
    CONTENT = """a;1;0;1;0"""

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader(objects_col=0)
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == ['a']
    assert dataset.attributes == list(map(str, range(4)))


def test_csv_reader_internal_objects2(tmp_path):
    CONTENT = """1;a;0;1;0"""

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader(objects_col=1)
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == ['a']
    assert dataset.attributes == list(map(str, range(4)))


def test_csv_reader_true_values(tmp_path):
    CONTENT = """a;0;b;1"""

    dataset_file = tmp_path / "test_dataset.csv"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as csvfile:
        csv_reader = CsvReader(set_true_values=set(['a', 'b']))
        dataset = csv_reader.read(csvfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True, False]]
    assert dataset.objects == ['0']
    assert dataset.attributes == list(map(str, range(4)))
