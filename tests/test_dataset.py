import pytest
from convertme import Dataset
import json


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


@pytest.mark.parametrize("objects,attributes,bools", [([0], [1, 2], [[True, True]]),
                                                      ([0, 1, 2], [1, 2], [
                                                       [True, True], [True, False], [False, True]]),
                                                      ([0], [1], [[True, ]])])
def test_dataset_to_json(objects, attributes, bools):
    objects = [0]
    attributes = [1, 2]
    bools = [[True, True]]

    json_string = Dataset(objects, attributes, bools).to_json()

    assert json.loads(json_string) == {
        'objects': objects, 'attributes': attributes, 'bools': bools}
