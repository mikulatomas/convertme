import pytest
from convertme import CsvWriter, Dataset
import io


def test_csv_writer(tmp_path):
    bools = [[True, False, True, False]]
    objects = ['0']
    attributes = list(map(str, range(4)))

    dataset = Dataset(objects, attributes, bools)

    output = io.StringIO()

    csv_writer = CsvWriter()

    csv_writer.write(dataset, output)

    OUTPUT = "objects;0;1;2;3\r\n0;1;0;1;0\r\n"

    assert output.getvalue() == OUTPUT
