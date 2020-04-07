import pytest
from convertme import CsvWriter, Dataset
from tests import load_all_test_files
import io
import os
import json

TEST_DATA_DIR_NO_PARAMETER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/no_parameter',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_NO_PARAMETER))
def test_csv_writer(data_file, json_file, tmpdir):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = str(tmpdir.join('test'))
        with open(output_path, 'w') as output:
            csv_writer = CsvWriter()
            csv_writer.write(dataset, output)

    # Read both files and comapre lines
    with open(data_file) as f:
        expected_output = f.readlines()

    with open(output_path) as f:
        output = f.readlines()

    assert expected_output == output


TEST_DATA_DIR_DELIMITER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/delimiter',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_DELIMITER))
def test_csv_writer_delimiter(data_file, json_file, tmpdir):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = str(tmpdir.join('test'))
        with open(output_path, 'w') as output:
            csv_writer = CsvWriter(delimiter=';')
            csv_writer.write(dataset, output)

    # Read both files and comapre lines
    with open(data_file) as f:
        expected_output = f.readlines()

    with open(output_path) as f:
        output = f.readlines()

    assert expected_output == output


TEST_DATA_DIR_OBJECT_LABELS = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/object_labels',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_OBJECT_LABELS))
def test_csv_writer_object_labels(data_file, json_file, tmpdir):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = str(tmpdir.join('test'))
        with open(output_path, 'w') as output:
            csv_writer = CsvWriter(write_object_labels=True)
            csv_writer.write(dataset, output)

    # Read both files and comapre lines
    with open(data_file) as f:
        expected_output = f.readlines()

    with open(output_path) as f:
        output = f.readlines()

    assert expected_output == output


TEST_DATA_DIR_ATTRIBUTE_LABELS = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/attribute_labels',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_ATTRIBUTE_LABELS))
def test_csv_writer_attribute_labels(data_file, json_file, tmpdir):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = str(tmpdir.join('test'))
        with open(output_path, 'w') as output:
            csv_writer = CsvWriter(write_attribute_labels=True)
            csv_writer.write(dataset, output)

    # Read both files and comapre lines
    with open(data_file) as f:
        expected_output = f.readlines()

    with open(output_path) as f:
        output = f.readlines()

    assert expected_output == output


TEST_DATA_DIR_LABELS = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data/labels',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR_LABELS))
def test_csv_writer_labels(data_file, json_file, tmpdir):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = str(tmpdir.join('test'))
        with open(output_path, 'w') as output:
            csv_writer = CsvWriter(
                write_attribute_labels=True, write_object_labels=True)
            csv_writer.write(dataset, output)

    # Read both files and comapre lines
    with open(data_file) as f:
        expected_output = f.readlines()

    with open(output_path) as f:
        output = f.readlines()

    assert expected_output == output
