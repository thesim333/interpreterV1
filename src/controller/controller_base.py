# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class ControllerBase(metaclass=ABCMeta):
    @abstractmethod
    def load_file(self, path):
        """Not Implemented"""

    @abstractmethod
    def pickle(self, args):
        """Not Implemented"""

    @abstractmethod
    def unpickle(self, args):
        """Not Implemented"""

    @abstractmethod
    def display(self, args):
        """Not Implemented"""

    @abstractmethod
    def save_to_database(self, args):
        """Not Implemented"""

    @abstractmethod
    def chart_pie(self, title, data, label=None):
        """Not Implemented"""

    @abstractmethod
    def chart_bar(self, title, x, y, top):
        """Not Implemented"""
