# Created by Simon Winder

from .validate_field import ValidateField
import re


class Sales(ValidateField):
    def validate(self):
        if re.match('^[0-9]{2,3}$', self._field) is not None:
            return self._valid
        else:
            return 'Sales must be 2 or 3 numbers'