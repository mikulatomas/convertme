from convertme import Dataset


class WriterInterface:
    def write(self, dataset: Dataset, output):
        """Takes Dataset and convert it into io stream"""
        return NotImplemented
