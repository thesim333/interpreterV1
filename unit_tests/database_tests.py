# Created by Simon Winder

import unittest
from src.database.myslq_database import DatabaseMySQL


class DatabaseUnitTests(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseMySQL()

    def test_update_record(self):
        sql_update = 'UPDATE Employee SET Age = 27 WHERE EmpID = "I123"'
        self.database.query(sql_update)
        sql_select = 'SELECT * FROM Employee WHERE EmpID = "I123"'
        x = self.database.select(sql_select)
        self.assertEqual(x[0][2], "27")
