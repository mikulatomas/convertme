import pytest
from convertme import BurmeisterWriter, Dataset
import io


def test_burmeister_writer(tmp_path):
    bools = [[True, False, True], [False, True, False]]
    objects = ['0', '1']
    attributes = list(map(str, range(3)))

    dataset = Dataset(objects, attributes, bools)

    output = io.StringIO()

    burmeister_writer = BurmeisterWriter()

    burmeister_writer.write(dataset, output)

    OUTPUT = """B

2
3
0
1
0
1
2
X.X
.X.
"""

    assert output.getvalue() == OUTPUT
