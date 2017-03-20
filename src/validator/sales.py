# Created by Simon Winder

from .validate_field import ValidateField
import re


class Sales(ValidateField):
    """
    Holds the sales field to be validated
    """
    def validate(self):
        """
        Validates if the field is a number with 2 or 3 digits
        :return: Sales must be 2 or 3 numbers
        """
        if re.match('^[0-9]{2,3}$', self._field) is not None:
            return self.VALID
        else:
            return 'Sales must be 2 or 3 numbers'
