import sys
import os
import yaml

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from readers.base_reader import BaseReader
from custom_object import CustomObject

class YamlReader(BaseReader):
    """Class to parse a YAML file given the file path."""

    def __init__(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.data = yaml.safe_load(file)
        except:
            print(f"\nERROR: Invalid YAML format.")
            sys.exit()


if __name__ == '__main__':
    reader = YamlReader("sample.yml")
    custom_object = CustomObject()
    custom_object.load(reader.data)
    custom_object.print()
    