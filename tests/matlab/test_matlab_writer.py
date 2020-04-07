import pytest
from convertme import MatlabWriter, MatlabReader, Dataset
import os
import json
from tests import load_all_test_files

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data_writer',
)


@pytest.mark.parametrize("data_file, json_file",
                         load_all_test_files(TEST_DATA_DIR))
def test_matlab_writer(data_file, json_file, tmpdir):
    # Load test input
    with open(json_file) as f:
        json_dict = json.load(f)
        dataset = Dataset(objects=json_dict['objects'],
                          attributes=json_dict['attributes'],
                          bools=json_dict['bools'])

        # Write output into file
        output_path = str(tmpdir.join('test'))
        with open(output_path, 'wb') as output:
            writer = MatlabWriter()
            writer.write(dataset, output)

    # Read both files and comapre lines
    reader = MatlabReader()
    with open(data_file, 'rb') as f:
        expected_dataset = reader.read(f)

    with open(output_path, 'rb') as f:
        output_dataset = reader.read(f)

    assert expected_dataset.bools == output_dataset.bools
