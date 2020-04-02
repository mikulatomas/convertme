import json
import functools


class Metadata:

    def __init__(self, objects, attributes, bools, src_url):
        self.objects = objects
        self.attributes = attributes
        self.number_of_objects = len(bools)
        self.number_of_attributes = len(bools[0])
        self.density = self.__calculate_density(bools)
        self.src_url = src_url

    def to_json(self):
        return json.dumps({'objects': self.objects,
                           'attributes': self.attributes,
                           'number_of_objects': self.number_of_objects,
                           'number_of_attributes': self.number_of_attributes,
                           'density': self.density,
                           'src_url': self.src_url})

    def __calculate_density(self, bools):
        total_number = len(bools) * len(bools[0])
        number_of_trues = 0

        for row in bools:
            number_of_trues += functools.reduce(lambda result, element:
                                                result + 1 if element else result,
                                                row, 0)

        return number_of_trues / total_number
