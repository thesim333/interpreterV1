# Created by Simon Winder

import re
from .validate_field import ValidateField


class Gender(ValidateField):
    def validate(self):
        if re.match('^(M|F)$', self._field) is not None:
            return self._valid
        else:
            return 'Not M or F'
