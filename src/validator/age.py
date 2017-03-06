from .validate_field import ValidateField
import re


class Age(ValidateField):
    def validate(self):
        if re.match('^[0-9]{3}$', self.field) is None:
            return 'Age must be 3 numbers'
        elif int(self.field) < 14 or int(self.field) > 81:
            return 'Age must be be 14 < 80'
        else:
            return self._valid
