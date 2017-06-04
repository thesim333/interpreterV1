# Created by Simon Winder

from .file_base import FileBase
import re


class FileReader(FileBase):
    """
    File reading class for reading in data to be verified
    """
    def get_file_data(self, file_path):
        """
        Read the data from file_path and return this data in rows - split
        :param file_path: the file
        :return: File contents or error
        """
        try:
            file_list = []
            file_object = open(file_path, 'r')

            for line in file_object:
                split_line = self.__into_parts(line)
                file_list.append(split_line)

            file_object.close()
            return file_list
        except FileNotFoundError as e:
            print(e)
            return None

    @staticmethod
    def __into_parts(line):
        """
        Splits the row into the needed parts
        :param line: the row
        :return: list of parts
        """
        parts = re.split("[\s,;]+", line.strip())
        return parts
