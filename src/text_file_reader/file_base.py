# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class FileBase(metaclass=ABCMeta):
    """
    Base class for getting input data from a text file
    """
    @abstractmethod
    def get_file_data(self, file_path):
        """Not Implemented"""
