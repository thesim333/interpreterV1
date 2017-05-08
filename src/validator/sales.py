# Created by Simon Winder

from .validate_field_number import ValidateFieldNumber
import re


class Sales(ValidateFieldNumber):
    """
    Holds the sales field to be validated
    """
    def validate(self):
        """
        Validates if the field is a number with 2 or 3 digits
        :return: Sales must be 2 or 3 numbers
        """
        if re.match('^[0-9]{2,3}$', self._field) is not None:
            self._field_number = int(self._field)
            return self.VALID
        else:
            return 'Sales must be 2 or 3 numbers'
