# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class DataFixerABC(metaclass=ABCMeta):
    def __init__(self, this_list):
        self._the_old_list = this_list
        self._the_new_list = [[], []]
        self.fix_the_list()

    @abstractmethod
    def fix_the_list(self):
        """not implemented"""

    def get_new_list_label(self):
        return self._the_new_list[0]

    def get_new_list_data(self):
        return self._the_new_list[1]
