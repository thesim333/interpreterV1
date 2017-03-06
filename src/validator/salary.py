from .validate_field import ValidateField
import re


class Salary(ValidateField):
    def validate(self):
        if re.match('^[0-9]{2,3}$', self.field) is not None:
            return self._valid
        else:
            return 'Salary must be 2 or 3 numbers'
