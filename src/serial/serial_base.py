# Created by Simon Winder

from abc import ABCMeta
from abc import abstractclassmethod


class SerialBase(metaclass=ABCMeta):
    """
    Abstract for a class that pickles and unpickles
    """
    @abstractclassmethod
    def pickle_this(self, file, content):
        """Not Implemented"""

    @abstractclassmethod
    def unpickle_this(self, file):
        """Not Implemented"""
