from convertme import ReaderInterface, Dataset


class FimiReader(ReaderInterface):

    def read(self, file) -> Dataset:
        lines = file.read().splitlines()
        max_attribute = 0
        values = []

        for line in lines:
            row_values = []

            for value in line.split():
                attribute = int(value)
                row_values.append(attribute)
                max_attribute = attribute if attribute > max_attribute else max_attribute

            values.append(row_values)

        bools = []

        for row in values:
            bools_row = [False for i in range(0, max_attribute + 1)]

            for attribute in row:
                bools_row[attribute] = True

            bools.append(bools_row)

        return Dataset(list(map(str, range(len(bools)))),
                       list(map(str, range(max_attribute + 1))),
                       bools)

