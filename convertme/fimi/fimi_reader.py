import math

from convertme import ReaderInterface, Dataset
from bitarray import bitarray


class FimiReader(ReaderInterface):
    def read(self, file):
        max_attribute = 0
        min_attribute = math.inf

        rows = []

        for line in file:
            # remove '\n' from line
            line = line.strip()
            row_attributes = []

            for value in line.split():
                attribute = int(value)
                row_attributes.append(attribute)
                max_attribute = max(attribute, max_attribute)
                min_attribute = min(attribute, min_attribute)

            rows.append(row_attributes)

        bools = [
            bitarray([True if i in row else False for i in range(min_attribute, max_attribute + 1)])
            for row in rows
        ]

        return Dataset(
            list(map(str, range(len(bools)))),
            list(map(str, range(min_attribute, max_attribute + 1))),
            bools,
        )
