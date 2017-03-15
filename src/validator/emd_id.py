# Created by Simon Winder

from .validate_field import ValidateField
import re


class EmpID(ValidateField):
    """
    Holds the employee ID field to be validated
    """
    def validate(self):
        """
        Tests the validity of the field
        :return: Valid or Employee ID must be of format "X000"
        """
        if re.match('^[A-Z][0-9]{3}$', self._field) is not None:
            return self._valid
        else:
            return 'Employee ID must be of format "X000"'
