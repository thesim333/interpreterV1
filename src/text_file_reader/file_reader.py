# Created by Simon Winder

from .file_base import FileBase
import re


class FileReader(FileBase):
    def get_file_data(self, file_path):
        try:
            file_list = []
            file_object = open(file_path, 'r')

            for line in file_object:
                split_line = self.__into_parts(line)
                file_list.append(split_line)

            return file_list
        except FileNotFoundError:
            return "File {} Not Found".format(file_path)

    @staticmethod
    def __into_parts(line):
        parts = re.split("[\s,;/]", line)
        return parts
