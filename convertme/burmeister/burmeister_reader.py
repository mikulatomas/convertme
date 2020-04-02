from convertme import ReaderInterface, Dataset


class BurmeisterReader(ReaderInterface):

    def __process_char(self, char):
        return char == 'X' or char == 'x'

    def read(self, file):
        bools = []
        lines = file.read().splitlines()

        if lines[0] != "B":
            raise ValueError("First line has to be \"B\"")

        obj_count = int(lines[2])
        att_count = int(lines[3])
        objects = []
        attributes = []

        for i in range(0, obj_count):
            objects.append(lines[5 + i])

        for i in range(0, att_count):
            attributes.append(lines[5 + obj_count + i])

        for i in range(obj_count + att_count + 5, len(lines)):
            bools.append(list(map(self.__process_char, lines[i])))

        return Dataset(objects, attributes, bools)
