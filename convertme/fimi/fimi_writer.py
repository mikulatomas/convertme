from convertme import WriterInterface, Dataset


class FimiWriter(WriterInterface):

    def write(self, dataset, output):
        lines = []

        for row in dataset.bools:
            attributes = []

            for attribute, _ in enumerate(row):
                if row[attribute]:
                    attributes.append(str(attribute))

            # remove f last space from line
            # ' '.join() is the fastest way to concatenate string
            lines.append(' '.join(attributes))

        output.write('\n'.join(lines) + '\n')
