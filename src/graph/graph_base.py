# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class GraphBase(metaclass=ABCMeta):
    """
    Abstract for Graph Class
    """
    @abstractmethod
    def plot_bar(self, title, x_label, y_label, items, data):
        pass

    @abstractmethod
    def plot_pie(self, title, items, data):
        pass
