from convertme import ReaderInterface, Dataset
import csv


class CsvReader(ReaderInterface):
    def __init__(self, objects=None, attributes=None, set_true_values=None,
                 delimiter=',', objects_col=None, attributes_row=None):

        if objects is not None and objects_col is not None:
            raise ValueError(
                "Object labels and objects colum cannot be specified in the same time.")

        if attributes is not None and attributes_row is not None:
            raise ValueError(
                "Attribute labels and attribute row cannot be specified in the same time.")

        if set_true_values is None:
            set_true_values = set(['1', 1])

        if type(set_true_values) is not set:
            raise ValueError("set_true_values must be a set.")

        if objects is None:
            self.objects = []
        else:
            self.objects = objects

        if attributes is None:
            self.attributes = []
        else:
            self.attributes = attributes

        self.set_true_values = set_true_values
        self.delimiter = delimiter
        self.objects_col = objects_col
        self.attributes_row = attributes_row

    def __process_char(self, char):
        return char in self.set_true_values

    def read(self, file):
        # default Python csv reader
        csv_reader = csv.reader(file, delimiter=self.delimiter)

        bools = []

        # if labels are specified, always prefer them
        # if labels are NOT specified, but objects_col or attributes_row is specified, extract them
        # generate the rest of the labels

        for idx, row in enumerate(csv_reader):
            if self.attributes_row == idx:
                # remove first string from header of the file -- 'id' etc.
                if self.objects_col is not None:
                    self.attributes = row[1:]
                else:
                    self.attributes = row
            else:
                # pop object label
                if type(self.objects_col) == int:
                    self.objects.append(row.pop(self.objects_col))

                bools.append(list(map(self.__process_char, row)))

        # generate labels if needed
        if not self.objects:
            self.objects = [str(label) for label in range(len(bools))]

        if not self.attributes:
            self.attributes = [str(label) for label in range(len(bools[0]))]

        return Dataset(self.objects, self.attributes, bools)
