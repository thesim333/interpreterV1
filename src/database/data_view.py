# written by Pippa Crawshaw - March 2017

from abc import ABCMeta, abstractmethod


class DatabaseViewBase(metaclass=ABCMeta):
    def __init__(self, database):
        self._database = database
        self._conn = None

    @abstractmethod
    def get_input(self, sql):
        """Not Implemented"""

    @abstractmethod
    def save_data_to_new(self, data_list):
        """Not Implemented"""

    @abstractmethod
    def _open_database(self):
        """Not Implemented"""

    @abstractmethod
    def _close_database(self):
        """Not Implemented"""

    @abstractmethod
    def _create_employee_table(self):
        """Not Implemented"""

    @abstractmethod
    def _insert_records(self, data_list):
        """Not Implemented"""
