# Created by Simon Winder

from .validate_field import ValidateField
import re


class BMI(ValidateField):
    """
    Contains a BMI field to be verified
    """
    def validate(self):
        """
        validates the BMI
        :return: Valid or not
        """
        if re.match('^(Normal|Overweight|Obesity|Underweight)$', self._field) is not None:
            return self._valid
        else:
            return 'BMI not a valid option'
