file_path = None
data = None

class BaseReader(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def print(self):
        """Print the contents of the base reader class."""
        print(f"\n--> File path: {self.file_path}")
        print(f"--> Data: {self.data}\n")

if __name__ == '__main__':
    base_reader = BaseReader("fake_path.fake")
    base_reader.print()

    