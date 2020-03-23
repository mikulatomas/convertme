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
