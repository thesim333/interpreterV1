# Created by Simon Winder

from .graph_base import GraphBase
import pandas as pd
import matplotlib.pyplot as plt


class Graph(GraphBase):
    """Class for creating charts"""
    __my_colors = 'rgbkymc'

    def plot_bar(self, title, x_label, y_label, items, data):
        """
        Creates a bar chart
        :param title: The chart title
        :param x_label: Axis X label
        :param y_label: Axis Y label
        :param items: Bar tags
        :param data: Bar data
        """
        if len(items) != len(data):
            return "Problem with item count could not create chart"

        info = pd.Series(data, index=items)
        plt.title(title)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
        ax = plt.gca()
        ax.tick_params(axis='x', colors='blue')
        ax.tick_params(axis='y', colors='blue')
        info.plot(kind='bar', color=self.__my_colors)
        plt.show()

    def plot_pie(self, title, items, data):
        """
        Creates a pie chart
        :param title: The chart title
        :param items: Section tags
        :param data: Section data
        :param data: Section data
        """
        fig1, ax1 = plt.subplots()
        ax1.pie(data, labels=items, autopct='%1.1f%%',
                shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(title)
        plt.show()
