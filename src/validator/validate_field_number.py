# Created by Simon Winder

from .validate_field import ValidateField
from abc import ABCMeta, abstractmethod


class ValidateFieldNumber(ValidateField):
    __metaclass__ = ABCMeta
    """
    ABC for validate field children that return an int
    """
    def __init__(self, field):
        super().__init__(field)
        self._field_number = 0

    @abstractmethod
    def validate(self):
        """Not Implemented"""

    def get_field(self):
        """
        The field as an integer
        :return: int
        """
        return self._field_number
