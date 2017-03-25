# Created by Simon Winder

from .creator_base import CreatorBase
from src.validator.employee import Employee
from src.validator.dob import DOB


class QueryCreator(CreatorBase):
    @staticmethod
    def get_pie_data_sum(data, labels):
        start = "SELECT {},SUM({}) FROM Employee ".format(labels, data)
        end = "GROUP BY {}".format(labels)
        return start + end

    @staticmethod
    def get_pie_data_count(data):
        start = "SELECT {0},COUNT({0})".format(data)
        end = " FROM Employee GROUP BY {0}".format(data)
        return start + end

    @staticmethod
    def get_bar_data(x, y, top):
        start = "SELECT {0},{1} FROM Employee ORDER BY ".format(x, y)
        end = "{0} LIMIT {1}".format(y, top)
        return start + end
