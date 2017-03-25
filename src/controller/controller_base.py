# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class ControllerBase(metaclass=ABCMeta):
    @abstractmethod
    def load_file(self, path):
        pass

    @abstractmethod
    def pickle(self, args):
        pass

    @abstractmethod
    def unpickle(self, args):
        pass

    @abstractmethod
    def display(self, args):
        pass

    @abstractmethod
    def save_to_database(self, args):
        pass

    @abstractmethod
    def chart_pie(self, title, data, label=None):
        pass

    @abstractmethod
    def chart_bar(self, title, x, y, top):
        pass
