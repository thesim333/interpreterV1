# Created by Simon Winder

import unittest
from src.validator.age import Age
from src.validator.bmi import BMI
from src.validator.emd_id import EmpID
from src.validator.gender import Gender
from src.validator.dob import DOB
from src.validator.salary import Salary
from src.validator.sales import Sales
from src.controller.controller import Controller
from src.controller.view import View
from src.validator.employee_builder import EmployeeBuilder
from src.validator.employee_director import EmployeeDirector
from src.validator.validate_field import ValidateField


class Assignment2Tests(unittest.TestCase):
    def setUp(self):
        self.valid_age = Age("34")
        self.valid_birthday = "09-08-1982"
        self.controller = Controller(View())

    def test_valid_age(self):
        self.assertEqual(self.valid_age.validate(), self.valid_age.get_valid())

    def test_invalid_age_1digit(self):
        invalid_age = Age("1")
        self.assertEqual(invalid_age.validate(), 'Age must be 2 numbers')

    def test_invalid_age_too_young(self):
        invalid_age = Age("12")
        self.assertEqual(invalid_age.validate(), 'Age must be be 14 < 80')

    def test_invalid_age_too_old(self):
        invalid_age = Age("96")
        self.assertEqual(invalid_age.validate(), 'Age must be be 14 < 80')

    def test_valid_age_return(self):
        self.valid_age.validate()
        self.assertEqual(self.valid_age.get_field(), 34)

    def test_valid_bmi_normal(self):
        bmi = BMI("Normal")
        self.assertEqual(bmi.validate(), bmi.get_valid())

    def test_valid_bmi_overweight(self):
        bmi = BMI("Overweight")
        self.assertEqual(bmi.validate(), bmi.get_valid())

    def test_valid_bmi_obesity(self):
        bmi = BMI("Obesity")
        self.assertEqual(bmi.validate(), bmi.get_valid())

    def test_valid_bmi_underweight(self):
        bmi = BMI("Underweight")
        self.assertEqual(bmi.validate(), bmi.get_valid())

    def test_invalid_bmi(self):
        bmi = BMI("RandomThing")
        self.assertEqual(bmi.validate(), 'BMI not a valid option')

    def test_valid_bmi_get_value(self):
        bmi = BMI("Normal")
        bmi.validate()
        self.assertEqual(bmi.get_field(), "Normal")

    def test_valid_emp_id(self):
        emp = EmpID("X234")
        self.assertEqual(emp.validate(), emp.get_valid())

    def test_invalid_emp_id(self):
        emp = EmpID("XX23")
        self.assertEqual(emp.validate(), 'Employee ID must be of format "X000"')

    def test_valid_emp_id_get_value(self):
        emp = EmpID("X234")
        emp.validate()
        self.assertEqual(emp.get_field(), "X234")

    def test_valid_gender_m(self):
        gender = Gender("M")
        self.assertEqual(gender.validate(), gender.get_valid())

    def test_valid_gender_f(self):
        gender = Gender("F")
        self.assertEqual(gender.validate(), gender.get_valid())

    def test_invalid_gender(self):
        gender = Gender("0")
        self.assertEqual(gender.validate(), 'Not M or F')

    def test_valid_gender_get_value(self):
        gender = Gender("M")
        gender.validate()
        self.assertEqual(gender.get_field(), "M")

    def test_valid_dob(self):
        dob = DOB(self.valid_birthday)
        self.assertEqual(dob.validate(), dob.get_valid())

    def test_invalid_dob_not_legal(self):
        dob = DOB("31-02-1992")
        self.assertEqual(dob.validate(), 'DOB is not a legal date')

    def test_invalid_dob_not_date(self):
        dob = DOB("fgghwedf")
        self.assertEqual(dob.validate(), 'DOB is not correct format')

    def test_age_dob(self):
        dob = DOB(self.valid_birthday)
        self.valid_age.validate()
        dob.validate()
        self.assertEqual(dob.check_age_against_date(self.valid_age.get_field()), dob.get_valid())

    def test_age_dob_invalid(self):
        dob = DOB(self.valid_birthday)
        age = Age("56")
        age.validate()
        dob.validate()
        self.assertEqual(dob.check_age_against_date(age.get_field()), 'Age does not match DOB')

    def test_valid_age_get_field(self):
        dob = DOB(self.valid_birthday)
        dob.validate()
        self.assertEqual(dob.get_field(), "1982-08-09")

    def test_valid_salary(self):
        salary = Salary("99")
        self.assertEqual(salary.validate(), salary.get_valid())

    def test_invalid_salary(self):
        salary = Salary("ss")
        self.assertEqual(salary.validate(), 'Salary must be 2 or 3 numbers')

    def test_valid_salary_get_value(self):
        salary = Salary("99")
        salary.validate()
        self.assertEqual(salary.get_field(), 99)

    def test_valid_sales(self):
        sales = Sales("99")
        self.assertEqual(sales.validate(), sales.get_valid())

    def test_invalid_sales(self):
        sales = Sales("ss")
        self.assertEqual(sales.validate(), 'Sales must be 2 or 3 numbers')

    def test_valid_sales_get_valud(self):
        sales = Sales("99")
        sales.validate()
        self.assertEqual(sales.get_field(), 99)

    def test_controller_chart_pie(self):
        self.assertEqual(self.controller.chart_pie('Sales by Gender', 'Sales', 'Gender'), True)

    def test_controller_chart_bar(self):
        self.assertEqual(self.controller.chart_bar('Top 10 Sales', 'EmpID', 'Sales', 10), True)

    def test_controller_chart_pie_other(self):
        self.assertEqual(self.controller.chart_pie('Staff Gender', 'Gender'), True)

    def test_employee_valid_input(self):
        the_list = ["E123", "M", "34", "99", "Normal", "99", self.valid_birthday]
        director = EmployeeDirector()
        builder = EmployeeBuilder(the_list)
        director.build_new_employee(builder)
        employee = builder.get_employee()
        self.assertEqual(employee.get_validity_or_reason_tags(), ValidateField.get_valid())
        self.assertEqual(employee.get_formatted_fields(), ['E123', 'M', 34, 99, 'Normal', 99, '1982-08-09'])

    def test_employee_missing_fields(self):
        result = self.controller._validate_contents(["E123", "M"], 0)
        self.assertEqual(result, '0 Not correct number of fields')

    def test_employee_invalid_fields(self):
        result = self.controller._validate_contents(["E123", "M", "23", "0", "Normal", "99", self.valid_birthday], 0)
        self.assertEqual(result, '0 Sales must be 2 or 3 numbers, Age does not match DOB')

    def test_employee_valid_input_controller(self):
        result = self.controller._validate_contents(["E123", "M", "34", "99", "Normal", "99", self.valid_birthday], 0)
        self.assertEqual(result, ['E123', 'M', 34, 99, 'Normal', 99, '1982-08-09'])

if __name__ == '__main__':
    unittest.main()
