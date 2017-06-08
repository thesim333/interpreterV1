# Created by Simon Winder

from .graph_builder import GraphBuilder
import pandas as pd
import matplotlib.pyplot as plt


class BarGraphBuilder(GraphBuilder):
    def __init__(self, db_view,  title, x, y, top):
        super().__init__(db_view, title)
        self.__x = x
        self.__y = y
        self.__top = top

    def create_chart_structure(self):
        info = pd.Series(self._data, index=self._label)
        ax = plt.gca()
        ax.tick_params(axis='x', colors='blue')
        ax.tick_params(axis='y', colors='blue')
        info.plot(kind='bar', color=self._my_colors)

    def set_titles(self):
        plt.title(self._title)
        plt.ylabel(self.__y)
        plt.xlabel(self.__x)

    def get_data_for_chart(self):
        sql = self.__get_query_string()
        self._get_data_from_db(sql)

    def get_chart(self):
        return plt

    def __get_query_string(self):
        start = "SELECT {0},{1} FROM Employee ORDER BY ".format(self.__x, self.__y)
        end = "{0} LIMIT {1}".format(self.__y, self.__top)
        return start + end
