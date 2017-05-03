# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod
from abc import abstractstaticmethod


class ViewBase(metaclass=ABCMeta):
    @abstractmethod
    def inject_controller(self, ctrl):
        """Not Implemented"""

    @abstractstaticmethod
    def output(message):
        """Not Implemented"""

    @abstractstaticmethod
    def get_input(message):
        """Not Implemented"""
