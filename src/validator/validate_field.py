# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class ValidateField(metaclass=ABCMeta):
    """
    Abstract class for fields to be validated
    """
    def __init__(self, field):
        self._field = field
        self._VALID = "Valid"

    @abstractmethod
    def validate(self):
        """Not Implemented"""

    def get_field(self):
        """
        Gets the field after validation
        :return: string
        """
        return self._field

    def get_valid(self):
        """
        "Valid" for tests of field validity
        :return: string "Valid"
        """
        return self._VALID
