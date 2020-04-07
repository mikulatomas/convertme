import pytest
from convertme import BurmeisterWriter, Dataset
from tests import load_all_test_files
import os
import json


TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data_writer',
)


@pytest.mark.parametrize("data_file, json_file",
                         load_all_test_files(TEST_DATA_DIR))
def test_burmeister_writer(data_file, json_file, tmpdir):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = str(tmpdir.join('test'))
        with open(output_path, 'w') as output:
            writer = BurmeisterWriter()
            writer.write(dataset, output)

    # Read both files and comapre lines
    with open(data_file) as f:
        expected_output = f.readlines()

    with open(output_path) as f:
        output = f.readlines()

    assert expected_output == output
