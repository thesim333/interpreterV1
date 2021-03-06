# Created by Simon Winder

import re
from .validate_field import ValidateField


class Gender(ValidateField):
    """
    Holds the gender of the employee to be validated
    """
    def validate(self):
        """
        Validates if the field is M or F
        :return: Valid or Not M or F
        """
        if re.match('^(M|F)$', self._field) is not None:
            return self.VALID
        else:
            return 'Not M or F'

    def get_field(self):
        return self._field
