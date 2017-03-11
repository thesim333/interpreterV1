# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class FileBase(metaclass=ABCMeta):
    @abstractmethod
    def get_file_data(self, file_path):
        pass
