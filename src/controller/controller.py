# Created by Simon Winder

import json
from src.text_file_reader.file_reader import FileReader
from src.database.myslq_database import DatabaseView
from src.graph.graph import Graph
from src.serial.serial import Serial
from src.validator.employee import Employee
from src.database.query_creator import QueryCreator
from .controller_base import ControllerBase


class Controller(ControllerBase):
    __view = None
    __file_view = None
    __database_view = None
    __graph_view = None
    __current_list = []
    __serial_file = None
    __query_creator = None
    __EMPID = 0

    def __init__(self, view):
        self.__view = view
        self.__file_view = FileReader()
        self.__database_view = DatabaseView()
        self.__graph_view = Graph()
        self.__query_creator = QueryCreator()
        with open('src\config.json') as json_data_file:
            data = json.load(json_data_file)
            self.__serial_file = data['pickle']['file']
            self.__database_name = data['mysql']['db']

    def load_file(self, path):
        """
        Reads a text file into __current_list
        :param path: the path of the file
        """
        data = self.__file_view.get_file_data(path)

        if data is not None:
            self.__validate_contents(data)
        else:
            self.__view.output(data)

    def __validate_contents(self, content):
        employee = Employee()
        self.__current_list = []
        for i, x in enumerate(content):
            result = employee.add_list(x)
            if 'fields' in result:
                self.__current_list.append(result['fields'])
            else:
                x = result['tags']
                self.__view.output('{} {}'.format(i, ' '.join(x)))

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
            self.__view.output("Too many parameters")
        elif len(self.__current_list) == 0:
            self.__view.output("No data to pickle")
        elif len(args) == 1:
            self.__view.output(Serial.pickle_this(args[0], self.__current_list))
        else:
            self.__view.output(Serial.pickle_this(self.__serial_file, self.__current_list))

    def unpickle(self, args):
        """
        Gets the data previously stored in a pickle.
        Places this in __current_list
        :args: overwrite or append
        """
        result = None
        if len(args) > 1:
            self.__view.output('Unpickle accepts one argument [overwrite or append]')
            return
        elif len(args) == 1:
            result = Serial.unpickle_this(args[0])
        else:
            result = Serial.unpickle_this(self.__serial_file)

        if result is not None:
            self.__current_list = result

    def display(self, args):
        if len(args) > 0:
            self.__view.output('display accepts no parameters')
        elif len(self.__current_list) > 0:
            for row in self.__current_list:
                self.__view.output(row)
        else:
            self.__view.output('No data to display')

    def save_to_database(self, args):
        if len(args) > 0:
            self.__view.output('display accepts no parameters')
        elif self.__current_list is []:
            self.__view.output('No data to save')
        else:
            self.__database_view.save_data_to_new(self.__database_name, self.__current_list)

    def chart_pie(self, title, data, label=None):
        sql = ''
        if label is not None:
            sql = self.__query_creator.get_pie_data_sum(data, label)
        else:
            sql = self.__query_creator.get_pie_data_count(data)
        new_list = self.__get_chart_data(sql)
        data_x = 1  # list numbers
        label_x = 0
        return self.__graph_view.plot_pie(title, new_list[label_x], new_list[data_x])

    def chart_bar(self, title, x, y, top):
        sql = self.__query_creator.get_bar_data(x, y, top)
        new_list = self.__get_chart_data(sql)
        x_pos = 0
        y_pos = 1
        return self.__graph_view.plot_bar(title, x, y, new_list[x_pos], new_list[y_pos])

    def __get_chart_data(self, sql):
        from_db = self.__database_view.get_input(self.__database_name, sql)
        return self.__fix_list(from_db)

    @staticmethod
    def __fix_list(from_db):
        print(from_db)
        new_list = [[], []]

        for i in from_db:
            new_list[0].append(i[0])
            new_list[1].append(i[1])

        return new_list
