import pytest
from convertme import FimiReader


def check_reader(CONTENT, tmp_path):
    dataset_file = tmp_path / "test_dataset.dat"
    dataset_file.write_text(CONTENT)

    with open(dataset_file, newline='') as fimifile:
        fimi_reader = FimiReader()
        dataset = fimi_reader.read(fimifile)

    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[False, True, True, False, True]]
    assert dataset.attributes == list(map(str, range(5)))
    assert dataset.objects == ['0']


def test_fimi_reader(tmp_path):
    CONTENT = """1 2 4"""
    check_reader(CONTENT, tmp_path)


def test_fimi_reader_tabs(tmp_path):
    CONTENT = """1\t2\t4"""
    check_reader(CONTENT, tmp_path)


def test_fimi_reader_more_spaces(tmp_path):
    CONTENT = """1  2      4"""
    check_reader(CONTENT, tmp_path)


def test_fimi_reader_space_at_the_end(tmp_path):
    CONTENT = """1 2 4 """
    check_reader(CONTENT, tmp_path)


def test_fimi_reader_space_at_the_begining(tmp_path):
    CONTENT = """ 1 2 4"""
    check_reader(CONTENT, tmp_path)


def test_fimi_reader_empty_line(tmp_path):
    CONTENT = """
1 2 4
"""
    dataset_file = tmp_path / "test_dataset.dat"
    dataset_file.write_text(CONTENT)
    with open(dataset_file, newline='') as fimifile:
        fimi_reader = FimiReader()
        dataset = fimi_reader.read(fimifile)
    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[False, False, False,
                              False, False], [False, True, True, False, True]]
    assert dataset.attributes == list(map(str, range(5)))
    assert dataset.objects == ['0', '1']

def test_fimi_reader_multiline_dataset(tmp_path):
    CONTENT = """1 2 4
0 1 2 3"""

    dataset_file = tmp_path / "test_dataset.dat"
    dataset_file.write_text(CONTENT)
    with open(dataset_file, newline='') as fimifile:
        fimi_reader = FimiReader()
        dataset = fimi_reader.read(fimifile)
    assert dataset_file.read_text() == CONTENT
    assert dataset.bools == [[False, True, True,
                              False, True], [True, True, True, True, False]]
    assert dataset.attributes == list(map(str, range(5)))
    assert dataset.objects == ['0', '1']