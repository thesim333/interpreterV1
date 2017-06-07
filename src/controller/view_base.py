# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod
from abc import abstractstaticmethod


class ViewBase(metaclass=ABCMeta):
    def __init__(self):
        self._controller = None

    def inject_controller(self, ctrl):
        self._controller = ctrl

    @abstractstaticmethod
    def get_input(message):
        """Not Implemented"""
