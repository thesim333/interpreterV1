# Created by Simon Winder


class EmployeeDirector(object):
    def __init__(self):
        self.__builder = None

    def build_new_employee(self, builder):
        self.__builder = builder
        self.__builder.add_emp_id()
        self.__builder.add_gender()
        self.__builder.add_age()
        self.__builder.add_sales()
        self.__builder.add_bmi()
        self.__builder.add_salary()
        self.__builder.add_dob()
