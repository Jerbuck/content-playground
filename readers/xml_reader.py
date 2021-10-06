import sys
import os
import xmltodict

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from readers.base_reader import BaseReader
from custom_object import CustomObject

class XmlReader(BaseReader):
    """Class to parse a XML file given the file path."""

    def __init__(self, file_path):
        try:
            with open(file_path, "r") as file:
                xml_contents = file.read()
                self.data = xmltodict.parse(xml_contents)['content']
        except:
            print(f"\nERROR: Invalid XML format.")
            sys.exit()

if __name__ == '__main__':
    reader = XmlReader("sample.xml")
    custom_object = CustomObject()
    custom_object.load(reader.data)
    custom_object.print()