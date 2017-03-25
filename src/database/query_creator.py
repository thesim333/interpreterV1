# Created by Simon Winder

from .creator_base import CreatorBase
from src.validator.employee import Employee
from src.validator.dob import DOB


class QueryCreator(CreatorBase):
    __insert_sql_start = """
                    INSERT INTO Employee (EmpID,Gender,Age,Sales,BMI,Salary,DOB)
                    VALUES (
                    """
    __insert_sql_end = ");"
    LINE = {0: 'EmpID',
            1: 'Gender',
            2: 'Age',
            3: 'Sales',
            4: 'BMI',
            5: 'Salary',
            6: "DATE_FORMAT(DOB, '%d-%m-%Y') AS dob"}

    def get_insert(self, line):
        temp_date = DOB(line[Employee.DOB])
        line[Employee.DOB] = temp_date.get_db_friendly()
        middle = ','.join(line)
        return self.__insert_sql_start + middle + self.__insert_sql_end

    def create_select(self, args):
        def get_val(n): return self.LINE[n]
        fields = list(map(get_val, args))
        start = "SELECT "
        middle = ','.join(fields)
        end = " FROM Employee"
        return start + middle + end

    def get_emp_id_test(self, emp_id):
        return "SELECT EmpID FROM Employee WHERE EmpID={}".format(emp_id)

    def get_pie_data_sum(self, data, labels):
        return "SELECT {1},SUM({0}) FROM Employee GROUP BY {1}".format(self.LINE[data], self.LINE[labels])

    def get_pie_data_count(self, data):
        return "SELECT {0},COUNT({0}) FROM Employee".format(self.LINE[data])

    @staticmethod
    def get_bar_data(x, y, top):
        return "SELECT TOP {2} {0},{1} FROM Employee ORDER BY {1}".format(x, y, top)
