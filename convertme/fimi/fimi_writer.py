from convertme import WriterInterface, Dataset


class FimiWriter(WriterInterface):

    def write(self, dataset: Dataset, output):
        for row in dataset.bools:
            content = ""

            for attribute in range(0, len(row)):
                if row[attribute]:
                    content += "{}".format(attribute) if (attribute == len(row) - 1) else "{} ".format(attribute)
            output.write(content)
