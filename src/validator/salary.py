# Created by Simon Winder

from .validate_field import ValidateField
import re


class Salary(ValidateField):
    """
    Holds the salary field to be validated
    """
    def validate(self):
        """
        Validates the field is a number with 2 or 3 digits
        :return: Valid or Salary must be 2 or 3 numbers
        """
        if re.match('^[0-9]{2,3}$', self._field) is not None:
            return self._valid
        else:
            return 'Salary must be 2 or 3 numbers'
