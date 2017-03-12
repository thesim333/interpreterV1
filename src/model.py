# written by Pippa Crawshaw
from src.validator.age import Age
# from src.validator.emd_id import EmpID
from src.validator.gender import Gender
# from src.validator.bmi import BMI
# from src.validator.sales import Sales
# from src.validator.salary import Salary
# from src.validator.dob import DOB

class Model(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        pass

    def employee_info(self, data_in_csv):
        for row in data_in_csv:
            if (row[0] != "emp_id"):
                emp_id = row[0]
                gender = Gender(row[1])
                result = gender.validate()
                print("gender:", row[1], ":", result)
                age = Age(row[2])
                # result = age.validate()
                sales = row[3]
                bmi = row[4]
                salary = row[5]
                dob = row[6]

        # age = Age(self.valid_age1)
        # self.assertEqual(age.validate(), self.valid)