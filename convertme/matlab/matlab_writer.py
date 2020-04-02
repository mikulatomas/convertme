from convertme import WriterInterface, Dataset
from mat4py import savemat


class MatlabWriter(WriterInterface):
    def write(self, dataset, output):
        data = {'M': dataset.bools}
        savemat(output, data)
