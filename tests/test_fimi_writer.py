import pytest
from convertme import FimiWriter, Dataset
import io


def test_csv_writer(tmp_path):
    bools = [[False, True, True, False, True]]
    objects = ['0']
    attributes = list(map(str, range(5)))

    dataset = Dataset(objects, attributes, bools)

    output = io.StringIO()

    csv_writer = FimiWriter()

    csv_writer.write(dataset, output)

    OUTPUT = """1 2 4\n"""

    assert output.getvalue() == OUTPUT
