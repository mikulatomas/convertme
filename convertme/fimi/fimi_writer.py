from convertme import WriterInterface, Dataset


class FimiWriter(WriterInterface):

    def write(self, dataset, output):

        for row in dataset.bools:
            attributes = []

            for attribute, _ in enumerate(row):
                if row[attribute]:
                    attributes.append(str(attribute))

            # remove f last space from line
            # ' '.join() is the fastest way to concatenate string
            output.write(' '.join(attributes) + '\n')
