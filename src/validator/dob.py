# Created by Simon Winder

from .validate_field import ValidateField
import re
import datetime


class DOB(ValidateField):
    correctDate = None

    def validate(self):
        if re.match('^[1-31]-[1-12]-[0-9]{4}$', self.field) is None:
            return 'DOB is not correct format'

        self.check_date()

        if self.correctDate is True:
            return self._valid
        else:
            return 'DOB is not a legal date'

    def check_date(self):
        day = re.match('^[1-31]', self.field).group(0)
        month = re.match('(?-)[1-12](?-)', self.field).group(0)
        year = re.match('[0-9]{4}$', self.field).group(0)

        try:
            new_date = datetime.datetime(int(year),int(month),int(day))
            self.correctDate = True
        except ValueError:
            self.correctDate = False
