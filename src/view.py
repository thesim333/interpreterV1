# written by Pippa Crawshaw

from abc import ABCMeta, abstractmethod


class View(metaclass=ABCMeta):
    @abstractmethod
    def output(self, message):
        pass

    @abstractmethod
    def get_input(self, message):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

