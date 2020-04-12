"""Unit test package for convertme."""
import os
import json
from convertme import Dataset
from bitarray import bitarray


class DatasetJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(
            self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if 'objects' in dct and 'attributes' in dct and 'bools' in dct:
            dataset = Dataset(objects=dct['objects'], attributes=dct['attributes'], bools=list(
                map(bitarray, dct['bools'])))
            return dataset
        return dct


def load_all_test_files(test_data_dir):
    data_files = []
    json_files = []

    directory = os.fsencode(test_data_dir)

    lst_dir = sorted(os.listdir(directory))
    for file in lst_dir:
        filename = os.fsdecode(file)
        filepath = os.path.join(test_data_dir, filename)
        if filename.endswith(".json"):
            json_files.append(filepath)
        else:
            data_files.append(filepath)

    return list(zip(data_files, json_files))
