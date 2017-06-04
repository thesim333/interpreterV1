# Created by Simon Winder

import json
from src.text_file_reader.file_reader import FileReader
from src.database.myslq_database import DatabaseView
from src.serial.serial import Serial
from src.validator.employee import Employee
from .controller_base import ControllerBase
from src.graph.graph_director import GraphDirector
from src.graph.pie_graph_builder import PieGraphBuilder
from src.graph.bar_graph_builder import BarGraphBuilder


class Controller(ControllerBase):
    def __init__(self, view):
        self.__current_list = []
        self.__view = view
        self.__file_view = FileReader()
        self.__EMPID = 0
        with open('src\config.json') as json_data_file:
            data = json.load(json_data_file)
            self.__serial_file = data['pickle']['file']
            self.__database_name = data['mysql']['db']
        self.__database_view = DatabaseView(self.__database_name)

    def load_file(self, path):
        """
        Reads a text file into __current_list
        :param path: the path of the file
        """
        data = self.__file_view.get_file_data(path)

        if data is not None:
            self.__validate_contents(data)
        else:
            print(data)

    def __validate_contents(self, content):
        employee = Employee()
        self.__current_list = []
        for i, x in enumerate(content):
            result = employee.add_list(x)
            if 'fields' in result:
                self.__current_list.append(result['fields'])
            else:
                x = result['tags']
                print('{} {}'.format(i, ' '.join(x)))

    def __to_lists(self, list_of_employees):
        self.__current_list = []
        for emp in list_of_employees:
            self.__current_list.append(emp.to_list())

    def pickle(self, args):
        """
        Pickles all the data currently loaded
        :param args: optional file name
        """
        if len(args) > 1:
            print("Too many parameters")
        elif len(self.__current_list) == 0:
            print("No data to pickle")
        elif len(args) == 1:
            print(Serial.pickle_this(args[0], self.__current_list))
        else:
            print(Serial.pickle_this(self.__serial_file, self.__current_list))

    def unpickle(self, args):
        """
        Gets the data previously stored in a pickle.
        Places this in __current_list
        :args: overwrite or append
        """
        result = None
        if len(args) > 1:
            print('Unpickle accepts one argument [overwrite or append]')
            return
        elif len(args) == 1:
            result = Serial.unpickle_this(args[0])
        else:
            result = Serial.unpickle_this(self.__serial_file)

        if result is not None:
            self.__current_list = result

    def display(self, args):
        """
        display the validated data to the screen
        :param args: user input args
        """
        if len(args) > 0:
            print('display accepts no parameters')
        elif len(self.__current_list) > 0:
            for row in self.__current_list:
                print(row)
        else:
            print('No data to display')

    def save_to_database(self, args):
        """
        Saves the data validated to the database
        :param args: User input args
        """
        if len(args) > 0:
            print('display accepts no parameters')
        elif self.__current_list is []:
            print('No data to save')
        else:
            self.__database_view.save_data_to_new(self.__current_list)

    def chart_pie(self, title, data, label=None):
        director = GraphDirector(PieGraphBuilder(self.__database_view, title, data, label))
        director.make_chart()
        return True

    def chart_bar(self, title, x, y, top):
        director = GraphDirector(BarGraphBuilder(self.__database_view, title, x, y, top))
        director.make_chart()
        return True

    # def chart_pie(self, title, data, label=None):
    #     """
    #     generates a sql and generates a pie chart with the queried data
    #     :param title: The chart title
    #     :param data: The data to be plotted
    #     :param label: The labels for the chart
    #     :return: True if plotted
    #     """
    #     sql = ''
    #     if label is not None:
    #         sql = self.__query_creator.get_pie_data_sum(data, label)
    #     else:
    #         sql = self.__query_creator.get_pie_data_count(data)
    #     to_plot = DataFixer(self.__get_chart_data(sql))
    #     return self.__graph_view.plot_pie(title, to_plot.get_new_list_label()
    #                                       , to_plot.get_new_list_data())

    # def chart_bar(self, title, x, y, top):
    #     """
    #     generates a sql and generates a bar chart with the queried data
    #     :param title: The chart title
    #     :param x: The data to be on axis x (label)
    #     :param y: The data to be on axis y
    #     :param top: The amount of results to graph
    #     :return: True if plotted
    #     """
    #     sql = self.__query_creator.get_bar_data(x, y, top)
    #     to_plot = DataFixer(self.__get_chart_data(sql))
    #     return self.__graph_view.plot_bar(title, x, y,
    #                                       to_plot.get_new_list_label(),
    #                                       to_plot.get_new_list_data())
