import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from custom_object import CustomObject
from readers.yaml_reader import YamlReader

class Test_YamlReader(unittest.TestCase):

    def test_custom_object_load_with_bad_file_path_verify_sys_exit_is_called(self):
        with self.assertRaises(SystemExit):
            custom_object = CustomObject()
            reader = YamlReader("bad-path.bad")
            custom_object.load(reader.data)

    def test_custom_object_load_with_invalid_file_verify_sys_exit_is_called(self):
        with self.assertRaises(SystemExit):
            custom_object = CustomObject()
            reader = YamlReader("sample.xml") #json works regardless
            custom_object.load(reader.data)
    
    def test_custom_object_load_with_good_data_verify_field_contents_are_correct(self):
        custom_object = CustomObject()
        reader = YamlReader("sample.yml")
        custom_object.load(reader.data)
        self.assertEqual(custom_object.username, "fake-username")    
        self.assertEqual(custom_object.password, "fake-password")  
        self.assertEqual(custom_object.base_url, "https://www.fake-url.com")
        self.assertEqual(len(custom_object.objects), 4)
        

if __name__ == '__main__':
    unittest.main()