import pytest
from convertme import BurmeisterReader


def write_read_dataset(tmp_path, content):
    dataset_file = tmp_path / "test_dataset.cxt"

    dataset_file.write_text(content)

    with open(dataset_file, newline='') as cxt_file:
        burmeister_reader = BurmeisterReader()
        dataset = burmeister_reader.read(cxt_file)
        assert dataset_file.read_text() == content
        return dataset


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

    dataset = write_read_dataset(tmp_path, CONTENT)

    assert dataset.bools == [[True, False, True], [False, True, False]]
    assert dataset.objects == ['firstObj', 'secondObj']
    assert dataset.attributes == ['firstAtt', 'secondAtt', 'thirdAtt']


def test_burmeister_reader_named(tmp_path):
    CONTENT = """B
someName
4
5
0
1
2
3
firstATT
1
2
3
4
x.x.X
.xX..
.x.x.
x...x"""
    dataset = write_read_dataset(tmp_path, CONTENT)

    assert dataset.bools == [
        [
            True, False, True, False, True], [
            False, True, True, False, False], [
                False, True, False, True, False], [
                    True, False, False, False, True]]
    assert dataset.objects == ['0', '1', '2', '3']
    assert dataset.attributes == ['firstATT', '1', '2', '3', '4']
