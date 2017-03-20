# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class EmployeeBase(metaclass=ABCMeta):
    @abstractmethod
    def employee_is_valid(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def get_bmi(self):
        pass

    @abstractmethod
    def get_dob(self):
        pass

    @abstractmethod
    def get_emp_id(self):
        pass

    @abstractmethod
    def get_gender(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_sales(self):
        pass

    @abstractmethod
    def get_invalid_flags(self):
        pass

    @abstractmethod
    def to_list(self):
        pass
