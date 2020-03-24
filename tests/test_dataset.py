import pytest
from convertme import Dataset


def test_empty_objects():
    with pytest.raises(ValueError):
        Dataset([], [1, 2], [[True, True]])


def test_empty_attributes():
    with pytest.raises(ValueError):
        Dataset([0], [], [[True, True]])


def test_empty_rows():
    with pytest.raises(ValueError):
        Dataset([0], [1, 2], [])


def test_empty_columns():
    with pytest.raises(ValueError):
        Dataset([0], [1, 2], [[]])


def test_objects_not_match():
    with pytest.raises(ValueError):
        Dataset([0], [1, 2], [[True, False], [True, True]])


def test_attributes_not_match():
    with pytest.raises(ValueError):
        Dataset([0, 1], [1], [[True, False], [True, True]])
