# Created by Simon Winder

from .validate_field import ValidateField
import re


class EmpID(ValidateField):
    def validate(self):
        if re.match('^[A-Z][0-9]{3}$', self._field) is not None:
            return self._valid
        else:
            return 'Employee ID must be of format "X000"'
