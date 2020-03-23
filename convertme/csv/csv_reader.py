from convertme import ReaderInterface, Dataset
import csv


class CsvReader(ReaderInterface):
    def __init__(self, objects=[], attributes=[], set_true_values=set('1'), delimiter=';'):
        self.objects = objects
        self.attributes = attributes
        self.set_true_values = set_true_values
        self.delimiter = delimiter

    def __process_char(self, char):
        return char in self.set_true_values

    def read(self, file):
        # default Python csv reader
        csv_reader = csv.reader(file, delimiter=self.delimiter)
        bools = []

        for row in csv_reader:
            bools.append(list(map(self.__process_char, row)))

        # test empty list
        if not self.objects:
            self.objects = [str(label) for label in range(len(bools))]

        if not self.attributes:
            self.attributes = [str(label) for label in range(len(bools[0]))]

        return Dataset(self.objects, self.attributes, bools)
