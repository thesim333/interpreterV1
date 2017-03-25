# Created by Simon Winder

from .validate_field import ValidateField
import re


class Age(ValidateField):
    """
    Contains an age field
    """
    __field_int = 0

    def validate(self):
        """
        Verifies the age is of 14 < x < 80
        :return: result
        """

        if re.match('^[0-9]{2}$', self._field) is None:
            return 'Age must be 2 numbers'
        elif int(self._field) < 15 or int(self._field) > 81:
            return 'Age must be be 14 < 80'
        else:
            self.__field_int = int(self._field)
            return self.VALID

    def get_field(self):
        return self.__field_int
