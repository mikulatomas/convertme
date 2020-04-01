import pytest
from convertme import CsvWriter, Dataset
from tests import load_all_test_files
import io
import os
import json

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data',
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR))
def test_writer(data_file, json_file, tmp_path):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = tmp_path / 'test'
        with open(output_path, 'w') as output:
            csv_writer = CsvWriter()
            csv_writer.write(dataset, output)

    # Read both files and comapre lines
    with open(data_file) as f:
        expected_output = f.readlines()

    with open(output_path) as f:
        output = f.readlines()

    assert expected_output == output

# def test_csv_writer(tmp_path):
#     bools = [[True, False, True, False]]
#     objects = ['0']
#     attributes = list(map(str, range(4)))

#     dataset = Dataset(objects, attributes, bools)

#     output = io.StringIO()

#     csv_writer = CsvWriter()

#     csv_writer.write(dataset, output)

#     OUTPUT = "objects,0,1,2,3\r\n0,1,0,1,0\r\n"

#     assert output.getvalue() == OUTPUT
