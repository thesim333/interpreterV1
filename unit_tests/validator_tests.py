# Created by Simon Winder

import unittest
from src.validator.age import Age
from src.validator.emd_id import EmpID
from src.validator.gender import Gender
from src.validator.bmi import BMI
from src.validator.sales import Sales
from src.validator.salary import Salary
from src.validator.dob import DOB
from src.validator.employee import Employee


class ValidatorUnitTests(unittest.TestCase):
    def setUp(self):
        self.valid_age1 = "34"
        self.valid_age2 = "23"
        self.bad_age1 = "1"
        self.bad_age2 = "000"
        self.bad_age3 = "X"
        self.bad_age4 = "13"
        self.valid_emp = "X234"
        self.bad_emp1 = "XX23"
        self.bad_emp2 = "1234"
        self.bad_emp3 = "X12"
        self.bad_emp4 = "123A"
        self.bad_emp5 = "a134"
        self.valid_gender1 = "M"
        self.valid_gender2 = "F"
        self.bad_gender1 = "MM"
        self.bad_gender2 = "MF"
        self.bad_gender3 = "X"
        self.valid_sales = "555"
        self.bad_sales1 = "0"
        self.bad_sales2 = "X"
        self.bad_sales3 = "1234"
        self.valid_bmi1 = "Normal"
        self.valid_bmi2 = "Overweight"
        self.valid_bmi3 = "Obesity"
        self.valid_bmi4 = "Underweight"
        self.bad_bmi = "Norma"
        self.valid_salary1 = "99"
        self.valid_salary2 = "123"
        self.valid_birthday = "09-08-1982"
        self.bad_birthday1 = "31-02-1992"
        self.bad_birthday2 = "31/02/1992"
        self.bad_birthday3 = "xx-xx-xxxx"

        self.valid = "Valid"

    def test_valid_age1(self):
        age = Age(self.valid_age1)
        self.assertEqual(age.validate(), self.valid)

    def test_valid_age2(self):
        age = Age(self.valid_age2)
        self.assertEqual(age.validate(), self.valid)

    def test_invalid_age1(self):
        age = Age(self.bad_age1)
        self.assertNotEqual(age.validate(), self.valid)

    def test_invalid_age2(self):
        age = Age(self.bad_age2)
        self.assertNotEqual(age.validate(), self.valid)

    def test_invalid_age3(self):
        age = Age(self.bad_age3)
        self.assertNotEqual(age.validate(), self.valid)

    def test_invalid_age4(self):
        age = Age(self.bad_age4)
        self.assertNotEqual(age.validate(), self.valid)

    def test_valid_emp(self):
        emp = EmpID(self.valid_emp)
        self.assertEqual(emp.validate(), self.valid)

    def test_invalid_emp1(self):
        emp = EmpID(self.bad_emp1)
        self.assertNotEqual(emp.validate(), self.valid)

    def test_invalid_emp2(self):
        emp = EmpID(self.bad_emp2)
        self.assertNotEqual(emp.validate(), self.valid)

    def test_invalid_emp3(self):
        emp = EmpID(self.bad_emp3)
        self.assertNotEqual(emp.validate(), self.valid)

    def test_invalid_emp4(self):
        emp = EmpID(self.bad_emp4)
        self.assertNotEqual(emp.validate(), self.valid)

    def test_invalid_emp5(self):
        emp = EmpID(self.bad_emp5)
        self.assertNotEqual(emp.validate(), self.valid)

    def test_valid_gender1(self):
        gen = Gender(self.valid_gender1)
        self.assertEqual(gen.validate(), self.valid)

    def test_valid_gender2(self):
        gen = Gender(self.valid_gender2)
        self.assertEqual(gen.validate(), self.valid)

    def test_invalid_gender1(self):
        gen = Gender(self.bad_gender1)
        self.assertNotEqual(gen.validate(), self.valid)

    def test_invalid_gender2(self):
        gen = Gender(self.bad_gender2)
        self.assertNotEqual(gen.validate(), self.valid)

    def test_invalid_gender3(self):
        gen = Gender(self.bad_gender3)
        self.assertNotEqual(gen.validate(), self.valid)

    def test_valid_sales(self):
        sal = Sales(self.valid_sales)
        self.assertEqual(sal.validate(), self.valid)

    def test_invalid_sales1(self):
        sal = Sales(self.bad_sales1)
        self.assertNotEqual(sal.validate(), self.valid)

    def test_invalid_sales2(self):
        sal = Sales(self.bad_sales2)
        self.assertNotEqual(sal.validate(), self.valid)

    def test_invalid_sales3(self):
        sal = Sales(self.bad_sales3)
        self.assertNotEqual(sal.validate(), self.valid)

    def test_valid_bmi1(self):
        bmi = BMI(self.valid_bmi1)
        self.assertEqual(bmi.validate(), self.valid)

    def test_valid_bmi2(self):
        bmi = BMI(self.valid_bmi2)
        self.assertEqual(bmi.validate(), self.valid)

    def test_valid_bmi3(self):
        bmi = BMI(self.valid_bmi3)
        self.assertEqual(bmi.validate(), self.valid)

    def test_valid_bmi4(self):
        bmi = BMI(self.valid_bmi4)
        self.assertEqual(bmi.validate(), self.valid)

    def test_invalid_bmi(self):
        bmi = BMI(self.bad_bmi)
        self.assertNotEqual(bmi.validate(), self.valid)

    def test_valid_salary1(self):
        sal = Salary(self.valid_salary1)
        self.assertEqual(sal.validate(), self.valid)

    def test_valid_salary2(self):
        sal = Salary(self.valid_salary2)
        self.assertEqual(sal.validate(), self.valid)

    def test_valid_dob(self):
        dob = DOB(self.valid_birthday)
        self.assertEqual(dob.validate(), self.valid)

    def test_invalid_dob1(self):
        dob = DOB(self.bad_birthday1)
        self.assertNotEqual(dob.validate(), self.valid)

    def test_invalid_dob2(self):
        dob = DOB(self.bad_birthday2)
        self.assertNotEqual(dob.validate(), self.valid)

    def test_invalid_dob3(self):
        dob = DOB(self.bad_birthday3)
        self.assertNotEqual(dob.validate(), self.valid)

    def test_valid_age_dob(self):
        dob = DOB(self.valid_birthday)
        age = Age(self.valid_age1)
        dob.validate()
        age.validate()
        actual = dob.check_age_against_date(age.get_field())
        expected = self.valid
        self.assertEqual(actual, expected)

    def test_invalid_age_dob(self):
        dob = DOB(self.valid_birthday)
        age = Age(self.valid_age2)
        age.validate()
        dob.validate()
        actual = dob.check_age_against_date(age.get_field())
        expected = self.valid
        self.assertNotEqual(actual, expected)

# emp, gender, age, sales, bmi, salary, dob
    def test_valid_employee(self):
        employee = Employee()
        actual = employee.add_list([self.valid_emp, self.valid_gender1, self.valid_age1,
                                    self.valid_sales, self.valid_bmi1, self.valid_salary1, self.valid_birthday])
        expected = {'validity': True, 'fields': ['X234', 'M', 34, 555, 'Normal', 99, '1982-08-09']}
        self.assertEqual(actual, expected)
