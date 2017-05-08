# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class DataFixerABC(metaclass=ABCMeta):
    """
    ABC that holds a list and the new lists from fixing
    """
    def __init__(self, this_list):
        self._the_old_list = this_list
        self._labels = []
        self._data = []
        self.fix_the_list()

    @abstractmethod
    def fix_the_list(self):
        """not implemented"""

    def get_new_list_label(self):
        """
        Gets the label part of the graph query
        :return: list []
        """
        return self._labels

    def get_new_list_data(self):
        """
        Gets the data part of the graph query
        :return: list []
        """
        return self._data
