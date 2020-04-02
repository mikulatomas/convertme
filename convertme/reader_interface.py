from convertme import Dataset


class ReaderInterface:
    def read(self, file) -> Dataset:
        """Load file and creates Dataset"""
        return NotImplemented
