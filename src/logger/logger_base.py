# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class Logger_Base(metaclass=ABCMeta):
    @abstractmethod
    def log_this(self, line, message):
        """Not Implemented"""
