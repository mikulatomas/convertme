import pytest
from convertme import FimiReader
import os
import json
from tests import load_all_test_files

TEST_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_data_reader',
)


@pytest.mark.parametrize("data_file, json_file",
                         load_all_test_files(TEST_DATA_DIR))
def test_csv_reader(data_file, json_file):
    # Load dataset file
    with open(data_file, newline='') as f:
        fimi_reader = FimiReader()
        dataset = fimi_reader.read(f)

    # Load expected output
    with open(json_file) as f:
        expected_json = json.load(f)

    # Compare
    assert expected_json == json.loads(dataset.to_json())


# def check_reader(CONTENT, tmpdir):
#     dataset_file = tmpdir / "test_dataset.dat"
#     dataset_file.write_text(CONTENT)
#
#     with open(dataset_file, newline='') as fimifile:
#         fimi_reader = FimiReader()
#         dataset = fimi_reader.read(fimifile)
#
#     assert dataset_file.read_text() == CONTENT
#     assert dataset.bools == [[False, True, True, False, True]]
#     assert dataset.attributes == list(map(str, range(5)))
#     assert dataset.objects == ['0']
#
#
# def test_fimi_reader(tmpdir):
#     CONTENT = """1 2 4"""
#     check_reader(CONTENT, tmpdir)
#
#
# def test_fimi_reader_tabs(tmpdir):
#     CONTENT = """1\t2\t4"""
#     check_reader(CONTENT, tmpdir)
#
#
# def test_fimi_reader_more_spaces(tmpdir):
#     CONTENT = """1  2      4"""
#     check_reader(CONTENT, tmpdir)
#
#
# def test_fimi_reader_space_at_the_end(tmpdir):
#     CONTENT = """1 2 4 """
#     check_reader(CONTENT, tmpdir)
#
#
# def test_fimi_reader_space_at_the_begining(tmpdir):
#     CONTENT = """ 1 2 4"""
#     check_reader(CONTENT, tmpdir)
#
#
# def test_fimi_reader_empty_line(tmpdir):
#     CONTENT = """
# 1 2 4
# """
#     dataset_file = tmpdir / "test_dataset.dat"
#     dataset_file.write_text(CONTENT)
#     with open(dataset_file, newline='') as fimifile:
#         fimi_reader = FimiReader()
#         dataset = fimi_reader.read(fimifile)
#     assert dataset_file.read_text() == CONTENT
#     assert dataset.bools == [[False, False, False,
#                               False, False], [False, True, True, False, True]]
#     assert dataset.attributes == list(map(str, range(5)))
#     assert dataset.objects == ['0', '1']

# def test_fimi_reader_multiline_dataset(tmpdir):
#     CONTENT = """1 2 4
# 0 1 2 3"""
#
#     dataset_file = tmpdir / "test_dataset.dat"
#     dataset_file.write_text(CONTENT)
#     with open(dataset_file, newline='') as fimifile:
#         fimi_reader = FimiReader()
#         dataset = fimi_reader.read(fimifile)
#     assert dataset_file.read_text() == CONTENT
#     assert dataset.bools == [[False, True, True,
#                               False, True], [True, True, True, True, False]]
#     assert dataset.attributes == list(map(str, range(5)))
#     assert dataset.objects == ['0', '1']
