import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from custom_object import CustomObject

class Test_CustomObject(unittest.TestCase):
    def test_custom_object_constructor_verifyy_fields_empty(self):
        custom_object = CustomObject()
        self.assertEqual(custom_object.username, None)
        self.assertEqual(custom_object.password, None)
        self.assertEqual(custom_object.base_url, None)
        self.assertEqual(custom_object.objects, [])

    def test_custom_object_print_verify_no_exception_raised(self):
        custom_object = CustomObject()
        custom_object.print()

    def test_custom_object_load_with_bad_data_verify_sys_exit_is_called(self):
        with self.assertRaises(SystemExit):
            custom_object = CustomObject()
            custom_object.load("bad-path.bad")

if __name__ == '__main__':
    unittest.main()