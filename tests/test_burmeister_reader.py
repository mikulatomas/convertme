import pytest
from convertme import BurmeisterReader


def test_burmeister_reader(tmp_path):
    CONTENT = """B

2
3
firstObj
secondObj
firstAtt
secondAtt
thirdAtt
X.X
.X."""

    dataset_file = tmp_path / "test_dataset.cxt"

    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as cxtfile:
        burmeister_reader = BurmeisterReader()
        dataset = burmeister_reader.read(cxtfile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[True, False, True], [False, True, False]]
    assert dataset.objects == ['firstObj', 'secondObj']
    assert dataset.attributes == ['firstAtt', 'secondAtt', 'thirdAtt']
