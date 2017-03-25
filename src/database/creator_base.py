# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class CreatorBase(metaclass=ABCMeta):

    @abstractmethod
    def create_select(self, args):
        pass

    @abstractmethod
    def get_insert(self, line):
        pass

    @abstractmethod
    def get_emp_id_test(self, emp_id):
        pass
