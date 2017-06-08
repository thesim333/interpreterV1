# Created by Simon Winder

from .employee_base import EmployeeBase
from .validate_field import ValidateField


class Employee(EmployeeBase):
    def __init__(self):
        self.__fields = {}
        self.__INDEX = ['EmpID', 'Gender', 'Age', 'Sales', 'BMI', 'Salary', 'DOB']

    def add_sales(self, sales):
        self.__fields["Sales"] = sales

    def add_age(self, age):
        self.__fields["Age"] = age

    def add_gender(self, gender):
        self.__fields["Gender"] = gender

    def add_salary(self, salary):
        self.__fields["Salary"] = salary

    def add_dob(self, dob):
        self.__fields["DOB"] = dob

    def add_bmi(self, bmi):
        self.__fields["BMI"] = bmi

    def add_emp_id(self, emp_id):
        self.__fields["EmpID"] = emp_id

    def get_validity_or_reason_tags(self):
        tags = []

        for key, field in self.__fields.items():
            val = field.validate()
            if val != ValidateField.get_valid():
                tags.append(val)

        age = self.__fields.get("Age").get_field()
        val = self.__fields.get("DOB").check_age_against_date(age)

        if val != ValidateField.get_valid():
            tags.append(val)

        return tags if len(tags) > 0 else ValidateField.get_valid()

    def get_formatted_fields(self):
        fields = []
        for i in self.__INDEX:
            fields.append(self.__fields[i].get_field())
        return fields
