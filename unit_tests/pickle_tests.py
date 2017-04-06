# Created by Simon Winder

import unittest
from src.serial.serial import Serial


class PickleTests(unittest.TestCase):
    def setUp(self):
        self.file_name = "test"

        a = {'EmpID': 'I123', 'Gender': 'M', 'Age': '23', 'Sales': '132',
             'BMI': 'Normal', 'Salary': '123', 'Birthday': '31-12-1989'}
        b = {'EmpID': 'I124', 'Gender': 'F', 'Age': '24', 'Sales': '133',
             'BMI': 'Normal', 'Salary': '124', 'Birthday': '31-12-1988'}

        self.the_list = [a, b]

    def test_pickle(self):
        actual = Serial.pickle_this(self.file_name, self.the_list)
        self.assertEqual(actual, 'All data pickled')

    def test_unpickle(self):
        x = Serial.unpickle_this(self.file_name)
        self.assertEqual(x, self.the_list)

    def test_failed_unpickle(self):
        bad_file = "y"
        actual = Serial.unpickle_this(bad_file)
        self.assertEqual(None, actual)

