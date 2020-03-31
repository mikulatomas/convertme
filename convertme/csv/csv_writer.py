from convertme import WriterInterface, Dataset
import csv


class CsvWriter(WriterInterface):
    def __init__(self, delimiter=','):
        self.delimiter = delimiter

    def write(self, dataset, output):
        csv_writer = csv.writer(output, delimiter=self.delimiter)

        csv_writer.writerow(['objects'] + dataset.attributes)

        for idx, row in enumerate(dataset.bools):
            csv_writer.writerow([dataset.objects[idx]] + list(map(int, row)))
