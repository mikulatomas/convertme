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

        for row in dataset.bools:
            output.write(''.join(map(self.__process_val, row)))
            output.write('\n')
