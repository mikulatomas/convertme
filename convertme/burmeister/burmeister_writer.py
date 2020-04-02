from convertme import WriterInterface, Dataset


class BurmeisterWriter(WriterInterface):
    def __process_val(self, b):
        return "X" if b else "."

    def write(self, dataset, output):
        content = ["B", "", str(len(dataset.objects)),
                   str(len(dataset.attributes))]

        output.writelines('\n'.join(content) + '\n\n')
        output.writelines('\n'.join(dataset.objects) + '\n')
        output.writelines('\n'.join(dataset.attributes) + '\n')

        data = []

        for row in dataset.bools:
            data.append(''.join(list(map(self.__process_val, row))))

        output.writelines('\n'.join(data) + '\n')
