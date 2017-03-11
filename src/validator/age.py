# Created by Simon Winder

from .validate_field import ValidateField
import re


class Age(ValidateField):
    def validate(self):
        if re.match('^[0-9]{2}$', self._field) is None:
            return 'Age must be 2 numbers'
        elif int(self._field) < 14 or int(self._field) > 81:
            return 'Age must be be 14 < 80'
        else:
            return self._valid
