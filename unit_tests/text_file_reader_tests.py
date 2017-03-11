# Created by Simon Winder

import unittest
from src.text_file_reader.file_reader import FileReader


class TextFileReaderTests(unittest.TestCase):
    def setUp(self):
        self.file_reader = FileReader()
        self.file_contents = [['A123', 'M', '23', '123', 'Normal', '39', '31-01-1992', ''], ['B123', 'F', '25', '234', 'Normal', '39', '25-12-1989']]
        self.file_not_found = r"File C:\Users\lamee\Documents\TestFile2.txt Not Found"

    def test_valid_file(self):
        file_path = r"C:\Users\lamee\Documents\TestFile1.txt"
        file_contents = self.file_reader.get_file_data(file_path)
        self.assertEqual(file_contents, self.file_contents)

    def test_file_not_found(self):
        file_path = r"C:\Users\lamee\Documents\TestFile2.txt"
        file_return = self.file_reader.get_file_data(file_path)
        self.assertEqual(file_return, self.file_not_found)

if __name__ == '__main__':
        unittest.main()
