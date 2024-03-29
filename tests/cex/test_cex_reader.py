import pytest
from convertme import CexReader
import os
import json
from tests import load_all_test_files

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "test_data_reader",
)


@pytest.mark.parametrize("data_file, json_file", load_all_test_files(TEST_DATA_DIR))
def test_cex_reader(data_file, json_file):
    # Load dataset file
    with open(data_file, mode="rb") as f:
        reader = CexReader()
        dataset = reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())
