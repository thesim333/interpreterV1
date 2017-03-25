# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod
from abc import abstractstaticmethod


class ViewBase(metaclass=ABCMeta):
    @abstractmethod
    def inject_controller(self, ctrl):
        pass

    @abstractstaticmethod
    def output(message):
        pass

    @abstractstaticmethod
    def get_input(message):
        pass
