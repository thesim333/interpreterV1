# Created by Simon Winder

from .validate_field import ValidateField
from .age_validate import AgeValidate
import re
from datetime import date
from dateutil.relativedelta import relativedelta


class DOB(ValidateField, AgeValidate):
    """
    Holds a DOB date to be validated
    Checks the DOB is valid to an age
    """
    __correctDate = None
    __date = None

    def validate(self):
        """
        Checks if the date is of the required format
        :return: Valid or reason the date is not valid
        """
        if re.match('^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$', self._field) is None:
            return 'DOB is not correct format'

        self.__check_date()

        if self.__correctDate is True:
            return self.VALID
        else:
            return 'DOB is not a legal date'

    def __check_date(self):
        """
        Checks if the date is a correct date
        Saves the result to __correctDate
        """
        date_fields = self._field.split('-')

        try:
            self.__date = date(int(date_fields[2]), int(date_fields[1]), int(date_fields[0]))
            self.__correctDate = True
        except ValueError:
            self.__correctDate = False

    def check_age_against_date(self, age):
        """
        Checks that the date and age are a match
        :param age: number value of a valid age
        :return: Valid or not
        """
        today = date.today()
        date_fields = self._field.split('-')
        self.__date = date(int(date_fields[2]), int(date_fields[1]), int(date_fields[0]))
        rd = relativedelta(today, self.__date)
        if rd.years == int(age):
            return self.VALID
        else:
            'Age does not match DOB'

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'t': DOB('12-12-1982')})
