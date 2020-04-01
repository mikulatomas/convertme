from convertme import ReaderInterface, Dataset
from mat4py import loadmat


class MatlabReader(ReaderInterface):

    def read(self, file):

        matlab_data = loadmat(file)
        matrix_name = next(iter(matlab_data))
        bools = matlab_data[matrix_name]
        objects = [str(label) for label in range(len(bools))]
        attributes = [str(label) for label in range(len(bools[0]))]
        dataset = Dataset(objects, attributes, bools)
        return dataset
