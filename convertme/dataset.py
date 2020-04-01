import json


class Dataset:
    """
    Inner structure of dataset
    """

    def __init__(self, objects, attributes, bools):
        if not objects:
            raise ValueError("objects cannot be empty")
        if not attributes:
            raise ValueError("attributes cannot be empty")

        if not bools:
            raise ValueError("bools cannot be empty")
        elif len(bools) > 1:
            if not len(bools[0]):
                raise ValueError("rows in bools cannot be empty")

        if len(objects) != len(bools):
            raise ValueError(
                "number of objects is not equal to number of rows")

        if len(attributes) != len(bools[0]):
            raise ValueError(
                "number of attributes is not equal to number of columns")

        self.objects = objects
        self.attributes = attributes
        self.bools = bools

    def to_json(self):
        return json.dumps({'objects': self.objects,
                           'attributes': self.attributes,
                           'bools': self.bools})
