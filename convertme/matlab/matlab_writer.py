from convertme import WriterInterface, Dataset
from mat4py import savemat
from bitarray import bitarray


class MatlabWriter(WriterInterface):
    def write(self, dataset, output):
        data = {'M': list(map(bitarray.tolist, dataset.bools))}
        savemat(output, data)
