# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class ValidateField(metaclass=ABCMeta):
    """
    Abstract class for fields to be validated
    """
    VALID = "Valid"

    def __init__(self, field):
        self._field = field

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def get_field(self):
        pass

    def get_valid(self):
        return self.VALID
