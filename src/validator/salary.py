# Created by Simon Winder

from .validate_field_number import ValidateFieldNumber
import re


class Salary(ValidateFieldNumber):
    """
    Holds the salary field to be validated
    """
    def validate(self):
        """
        Validates the field is a number with 2 or 3 digits
        :return: Valid or Salary must be 2 or 3 numbers
        """
        if re.match('^[0-9]{2,3}$', self._field) is not None:
            self._field_number = int(self._field)
            return self._VALID
        else:
            return 'Salary must be 2 or 3 numbers'
