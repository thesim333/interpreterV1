# Created by Simon Winder

from .graph_builder import GraphBuilder
import matplotlib.pyplot as plt


class PieGraphBuilder(GraphBuilder):
    def __init__(self, db_view, title, data, label=None):
        super().__init__(db_view, title)
        self.__before_data = data
        self.__before_label = label

    def create_chart_structure(self):
        plt.pie(self._data, labels=self._label, autopct='%1.1f%%', shadow=True, startangle=90, colors=self._my_colors)
        plt.axis('equal')

    def set_titles(self):
        plt.title(self._title)

    def get_data_for_chart(self):
        sql = ''
        if self.__before_label is None:
            sql = self.__get_pie_data_count()
        else:
            sql = self.__get_pie_data_sum()
        self._get_data_from_db(sql)

    def get_chart(self):
        plt.show()

    def __get_pie_data_sum(self):
        start = "SELECT {},SUM({}) FROM Employee ".format(self.__before_label, self.__before_data)
        end = "GROUP BY {}".format(self.__before_label)
        return start + end

    def __get_pie_data_count(self):
        start = "SELECT {0},COUNT({0})".format(self.__before_data)
        end = " FROM Employee GROUP BY {0}".format(self.__before_data)
        return start + end
