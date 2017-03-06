# Created by Simon Winder

from .validate_field import ValidateField
import re


class BMI(ValidateField):
    def validate(self):
        if re.match('^(Normal|Overweight|Obesity|Underweight)$', self.field) is not None:
            return self._valid
        else:
            return 'BMI not a valid option'
