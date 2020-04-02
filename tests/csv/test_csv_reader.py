import pytest
from convertme import CsvReader
import os
import json
from tests import load_all_test_files

TEST_DATA_DIR_NO_PARAMETER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/no_parameter',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_NO_PARAMETER))
def test_csv_reader(data_file, json_file):
    # Load dataset file
    with open(data_file, newline='') as f:
        csv_reader = CsvReader()
        dataset = csv_reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())


TEST_DATA_DIR_DELIMITER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/delimiter',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_DELIMITER))
def test_csv_reader_delimiter(data_file, json_file):
    # Load dataset file
    with open(data_file, newline='') as f:
        csv_reader = CsvReader(delimiter=';')
        dataset = csv_reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())


TEST_DATA_DIR_OBJECT_LABELS = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/object_labels',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_OBJECT_LABELS))
def test_csv_reader_object_labels(data_file, json_file):
    # Load dataset file
    with open(data_file, newline='') as f:
        csv_reader = CsvReader(objects_col=0)
        dataset = csv_reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())


TEST_DATA_DIR_LABELS = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/labels',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_LABELS))
def test_csv_reader_labels(data_file, json_file):
    # Load dataset file
    with open(data_file, newline='') as f:
        csv_reader = CsvReader(objects_col=0, attributes_row=0)
        dataset = csv_reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())


TEST_DATA_DIR_ATTRIBUTE_LABELS = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/attribute_labels',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_ATTRIBUTE_LABELS))
def test_csv_reader_attribute_labels(data_file, json_file):
    # Load dataset file
    with open(data_file, newline='') as f:
        csv_reader = CsvReader(attributes_row=0)
        dataset = csv_reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())


TEST_DATA_DIR_ATTRIBUTE_LABELS = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/external_labels',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_ATTRIBUTE_LABELS))
def test_csv_reader_external_labels(data_file, json_file):
    # Load dataset file
    with open(data_file, newline='') as f:
        csv_reader = CsvReader(
            objects=['obj0', 'obj1'], attributes=['attr0', 'attr1'])
        dataset = csv_reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())


def test_csv_reader_object_labels_exception():
    with pytest.raises(ValueError):
        CsvReader(objects=[0, 1, 3], objects_col=0)


def test_csv_reader_attribute_labels_exception():
    with pytest.raises(ValueError):
        CsvReader(attributes=[0, 1, 3], attributes_row=0)


def test_csv_reader_true_values_exception():
    with pytest.raises(ValueError):
        CsvReader(set_true_values=[1, 2, 3])
