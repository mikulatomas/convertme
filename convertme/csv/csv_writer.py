from convertme import WriterInterface, Dataset
import csv


class CsvWriter(WriterInterface):
    def __init__(self, delimiter=',', write_object_labels=False, write_attribute_labels=False):
        self.delimiter = delimiter
        self.write_object_labels = write_object_labels
        self.write_attribute_labels = write_attribute_labels

    def write(self, dataset, output):
        csv_writer = csv.writer(output, delimiter=self.delimiter)

        if self.write_attribute_labels:
            if self.write_object_labels:
                csv_writer.writerow(['objects'] + dataset.attributes)
            else:
                csv_writer.writerow(dataset.attributes)

        for idx, row in enumerate(dataset.bools):
            if self.write_object_labels:
                csv_writer.writerow(
                    [dataset.objects[idx]] + list(map(int, row)))
            else:
                csv_writer.writerow(list(map(int, row)))
