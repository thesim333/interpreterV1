# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class EmployeeBase(metaclass=ABCMeta):
    @abstractmethod
    def add_list(self, employee_list):
        """Not Implemented"""
