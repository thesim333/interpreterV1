# Created by Simon Winder

from .validate_field import ValidateField
from .age_validate import AgeValidate
import re
from datetime import date
from dateutil.relativedelta import relativedelta


class DOB(ValidateField, AgeValidate):
    __correctDate = None
    __date = None

    def validate(self):
        if re.match('^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$', self._field) is None:
            return 'DOB is not correct format'

        self.__check_date()

        if self.__correctDate is True:
            return self._valid
        else:
            return 'DOB is not a legal date'

    def __check_date(self):
        date_fields = self._field.split('-')

        try:
            self.__date = date(int(date_fields[2]), int(date_fields[1]), int(date_fields[0]))
            self.__correctDate = True
        except ValueError:
            self.__correctDate = False

    def check_age_against_date(self, age):
        today = date.today()
        date_fields = self._field.split('-')
        self.__date = date(int(date_fields[2]), int(date_fields[1]), int(date_fields[0]))
        rd = relativedelta(today, self.__date)
        if rd.years == int(age):
            return self._valid
        else:
            'Age does not match DOB'
