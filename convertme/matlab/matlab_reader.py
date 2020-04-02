from convertme import ReaderInterface, Dataset
from mat4py import loadmat
import h5py
from numpy import transpose


class MatlabReader(ReaderInterface):

    def read(self, file):

        try:
            matlab_data = loadmat(file)
        except BaseException:
            f = h5py.File(file, 'r')
            key = list(f.keys())[0]
            data = f[key]
            matlab_data = {key: transpose(data).tolist()}

        matrix_name = next(iter(matlab_data))
        bools = matlab_data[matrix_name]
        objects = [str(label) for label in range(len(bools))]
        attributes = [str(label) for label in range(len(bools[0]))]
        dataset = Dataset(objects, attributes, bools)
        return dataset
