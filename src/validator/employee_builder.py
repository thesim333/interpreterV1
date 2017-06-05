# Created by Simon Winder

from .employee import Employee
from .age import Age
from .salary import Salary
from .sales import Sales
from .dob import DOB
from .emd_id import EmpID
from .gender import Gender
from .bmi import BMI


class EmployeeBuilder(object):
    def __init__(self, line):
        self.__line = line
        self.__employee = Employee()
        self.__INDEX = {'EmpID': 0, 'Gender': 1, 'Age': 2, 'Sales': 3, 'BMI': 4, 'Salary': 5, 'DOB': 6}

    def add_emp_id(self):
        emp_id = EmpID(self.__line[self.__INDEX['EmpID']])
        self.__employee.add_emp_id(emp_id)

    def add_gender(self):
        gender = Gender(self.__line[self.__INDEX['Gender']])
        self.__employee.add_gender(gender)

    def add_age(self):
        age = Age(self.__line[self.__INDEX['Age']])
        self.__employee.add_age(age)

    def add_sales(self):
        sales = Sales(self.__line[self.__INDEX['Sales']])
        self.__employee.add_sales(sales)

    def add_bmi(self):
        bmi = BMI(self.__line[self.__INDEX['BMI']])
        self.__employee.add_bmi(bmi)

    def add_salary(self):
        salary = Salary(self.__line[self.__INDEX['Salary']])
        self.__employee.add_salary(salary)

    def add_dob(self):
        dob = DOB(self.__line[self.__INDEX['DOB']])
        self.__employee.add_dob(dob)

    def get_employee(self):
        return self.__employee
