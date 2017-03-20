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
    __fields = []
    __class_fields = [EmpID, Gender, Age, Sales, BMI, Salary, DOB]
    __is_valid = True
    __invalid_flags = []
    __FIELDS_TOTAL = 7
    __NOT_CORRECT_NUMBER = 'Not correct number of fields'
    EMP_ID = 0
    GENDER = 1
    AGE = 2
    SALES = 3
    BMI = 4
    SALARY = 5
    DOB = 6

    def __init__(self, employee_list):
        """
        constructor for an line of employee data
        :param employee_list: list of fields to be validated
        """
        self.__from_list(employee_list)

    def __from_list(self, employee_list):
        if len(employee_list) == self.__FIELDS_TOTAL:
            self.__make_fields(employee_list)
            self.__validate_all()
        else:
            self.__add_invalid_flag(self.__NOT_CORRECT_NUMBER)
            self.__is_valid = False

    def __add_invalid_flag(self, flag):
        self.__invalid_flags.append(flag)

    def __make_fields(self, employee_list):
        for index in range(employee_list):
            self.__fields.append(self.__class_fields[index](employee_list[index]))

    def __validate_all(self):
        for thing in self.__class_fields:
            x = thing.validate()

            if x != ValidateField.VALID:
                self.__is_valid = False
                self.__add_invalid_flag(x)

    def employee_is_valid(self):
        """
        Method to get if the line is valid
        Line is all valid if all the fields are valid
        :return: True or False
        """
        return self.__is_valid

    def get_invalid_flags(self):
        """
        Gets a list of all the invalid flags generated by the validating the line
        :return: List of Strings
        """
        return self.__invalid_flags

    def get_age(self):
        """
        Gets the line age field
        :return: Age field as a string
        """
        return self.__fields[self.AGE].get_field()

    def get_bmi(self):
        """
        Gets the line bmi field
        :return: BMI field as a string
        """
        return self.__fields[self.BMI].get_field()

    def get_dob(self):
        """
        Gets the line dob field
        :return: BOB field as a string
        """
        return self.__fields[self.DOB].get_field()

    def get_emp_id(self):
        """
        Gets the line employee id field
        :return: Employee ID field as a string
        """
        return self.__fields[self.EMP_ID].get_field()

    def get_gender(self):
        """
        Gets the line gender field
        :return: Gender field as a string
        """
        return self.__fields[self.GENDER].get_field()

    def get_salary(self):
        """
        Gets the line salary field
        :return: Salary field as a string
        """
        return self.__fields[self.SALARY].get_field()

    def get_sales(self):
        """
        Gets the line sales field
        :return: Sales field as a string
        """
        return self.__fields[self.SALES].get_field()

    def to_list(self):
        text_list = []

        for field in self.__fields:
            text_list.append(field.get_field())

        return text_list
