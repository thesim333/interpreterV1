# Created by Simon Winder

from .validate_field import ValidateField
import re


class Salary(ValidateField):
    """
    Holds the salary field to be validated
    """
    __field_int = 0

    def validate(self):
        """
        Validates the field is a number with 2 or 3 digits
        :return: Valid or Salary must be 2 or 3 numbers
        """
        if re.match('^[0-9]{2,3}$', self._field) is not None:
            self.__field_int = int(self._field)
            return self.VALID
        else:
            return 'Salary must be 2 or 3 numbers'

    def get_field(self):
        return self.__field_int
