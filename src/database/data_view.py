# written by Pippa Crawshaw - March 2017

from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    @abstractmethod
    def get_input(self, database_file_name, sql):
        """Not Implemented"""

    @abstractmethod
    def save_data_to_new(self, file_name, data_list):
        """Not Implemented"""
