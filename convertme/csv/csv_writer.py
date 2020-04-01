from convertme import WriterInterface, Dataset
import csv


class CsvWriter(WriterInterface):
    def __init__(self, delimiter=',', write_labels=False):
        self.delimiter = delimiter
        self.write_labels = write_labels

    def write(self, dataset, output):
        csv_writer = csv.writer(output, delimiter=self.delimiter)

        if self.write_labels:
            csv_writer.writerow(['objects'] + dataset.attributes)

            for idx, row in enumerate(dataset.bools):
                csv_writer.writerow(
                    [dataset.objects[idx]] + list(map(int, row)))
        else:
            for idx, row in enumerate(dataset.bools):
                csv_writer.writerow(list(map(int, row)))
