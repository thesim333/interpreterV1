# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class EmployeeBase(metaclass=ABCMeta):
    @abstractmethod
    def add_emp_id(self, emp_id):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_salary(self, salary):
        pass

    @abstractmethod
    def add_sales(self, sales):
        pass

    @abstractmethod
    def add_dob(self, dob):
        pass

    @abstractmethod
    def add_bmi(self, bmi):
        pass

    @abstractmethod
    def add_gender(self, gender):
        pass
