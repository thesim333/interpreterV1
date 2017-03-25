# Created by Simon Winder

import unittest
from src.text_file_reader.file_reader import FileReader


class TextFileReaderTests(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader()
        self.file_contents = [['A123', 'M', '23', '123', 'Normal', '39', '31-01-1992', ''],
                              ['B123', 'F', '25', '234', 'Normal', '39', '25-12-1989']]

    def test_valid_file(self):
        file_path = ""
        file_contents = self.file_reader.get_file_data(file_path)
        self.assertEqual(file_contents, self.file_contents)

    def test_file_not_found(self):
        file_path = "TestFile2.txt"
        file_return = self.file_reader.get_file_data(file_path)
        self.assertRaises(FileNotFoundError)

if __name__ == '__main__':
        unittest.main()
