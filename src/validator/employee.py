# Created by Simon Winder

from .age import Age
from .bmi import BMI
from .dob import DOB
from .emd_id import EmpID
from .gender import Gender
from .salary import Salary
from .sales import Sales
from .employee_base import EmployeeBase
from .validate_field import ValidateField


class Employee(EmployeeBase):
    """
    Holds all the fields of employee data
    Checks if the whole line is valid
    """
    def __init__(self):
        self.__FIELDS_TOTAL = 7
        self.__NOT_CORRECT_NUMBER = 'Not correct number of fields'
        self.__INDEX = {'EmpID': 0, 'Gender': 1, 'Age': 2, 'Sales': 3, 'BMI': 4, 'Salary': 5, 'DOB': 6}

    def add_list(self, employee_list):
        if len(employee_list) != self.__FIELDS_TOTAL:
            print(len(employee_list))
            return {'tags': [self.__NOT_CORRECT_NUMBER]}

        validity = self.__validate(employee_list)

        if 'fields' in validity:
            return self.__fix_fields(validity)
        else:
            return validity

    @staticmethod
    def __fix_fields(validity):
        fields = validity['fields']
        validity['fields'] = []

        for field in fields:
            validity['fields'].append(field.get_field())

        return validity

    # def __add_invalid_flag(self, flag):
        # self.__invalid_flags.append(flag)

    def __validate(self, employee_list):
        my_fields = []
        tags = []
        is_valid = True

        my_fields.append(EmpID(employee_list[0]))
        my_fields.append(Gender(employee_list[1]))
        my_fields.append(Age(employee_list[2]))
        my_fields.append(Sales(employee_list[3]))
        my_fields.append(BMI(employee_list[4]))
        my_fields.append(Salary(employee_list[5]))
        my_fields.append(DOB(employee_list[6]))

        for i in my_fields:
            val = i.validate()
            if val != ValidateField.get_valid():
                is_valid = False
                tags.append(val)

        age = my_fields[self.__INDEX['Age']].get_field()
        val = my_fields[self.__INDEX['DOB']].check_age_against_date(age)
        if val != ValidateField.get_valid():
            tags.append(val)
            is_valid = False

        # if tags is []:
        if is_valid is True:
            return {'fields': my_fields}
        else:
            return {'tags': tags}
