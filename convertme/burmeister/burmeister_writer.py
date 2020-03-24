from convertme import WriterInterface, Dataset



class BurmeisterWriter(WriterInterface):
    def __process_val(self, b):
        return "X" if b else "."

    def __write_list(self, lst, output):
        for s in lst:
            output.write(s)
            output.write("\n")
    
    def write(self, dataset, output):
        content = ["B", "", str(len(dataset.objects)), str(len(dataset.attributes))]
        self.__write_list(content, output)
        self.__write_list(dataset.objects, output)
        self.__write_list(dataset.attributes, output)
        data=[]
        for idx,row in enumerate(dataset.bools):
            data.append(''.join(list(map(self.__process_val, row))))
        self.__write_list(data, output)

