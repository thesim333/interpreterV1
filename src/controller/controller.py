# Created by Simon Winder

import json
from src.text_file_reader.file_reader import FileReader
from src.database.myslq_database import DatabaseMySQL
from src.graph.graph import Graph
from src.serial.serial import Serial
from src.validator.employee import Employee
from src.database.query_creator import QueryCreator
from src.logger.logger import Logger
from src.validator.validate_field import ValidateField


class Controller:
    __view = None
    __file_view = None
    __database_view = None
    __graph_view = None
    __current_list = None
    __serial_file = None
    __query_creator = None

    def __init__(self, view):
        self.__view = view
        self.__file_view = FileReader()
        self.__database_view = DatabaseMySQL()
        self.__graph_view = Graph()
        self.__query_creator = QueryCreator()
        self.__logger = Logger()
        with open('src\config.json') as json_data_file:
            self.__serial_file = json.load(json_data_file)['pickle']['file']

    def load_file(self, path):
        data = self.__file_view.get_file_data(path)

        if data == FileNotFoundError:
            self.__view.output(data)
        else:
            self.__validate_contents(data)

    def __validate_contents(self, content):
        employee = Employee()
        self.__current_list = []
        for i, x in enumerate(content):
            result = employee.add_list(x)
            if result is ValidateField.VALID:
                self.__view.output("{} {}".format(i, result))


    def __to_lists(self, list_of_employees):
        self.__current_list = []
        for emp in list_of_employees:
            self.__current_list.append(emp.to_list())

    def pickle(self, args):
        if len(args) > 0:
            self.__view.output("Pickle accepts no parameters")
        elif self.__current_list is []:
            self.__view.output("No data to pickle")
        else:
            Serial.pickle_this(self.__serial_file, self.__current_list)
            self.__current_list = []

    def unpickle(self, args):
        """
        Gets the data previously stored in a pickle.
        Places this in __current_list
        :args: overwrite or append
        """
        overwrite = 'overwrite'
        append = 'append'
        option = overwrite

        if len(args) > 1:
            self.__view.output('Unpickle accepts one argument [overwrite or append]')
            return
        elif len(args) == 1 and str.lower(args[0]) == overwrite:
            option = overwrite
        elif len(args) == 1 and str.lower(args[0]) == append:
            option = append

        from_pickle = Serial.unpickle_this(self.__serial_file)

        if from_pickle == FileNotFoundError:
            self.__view.output(from_pickle)
        elif option == overwrite:
            self.__current_list = from_pickle
        else:
            self.__current_list.extend(from_pickle)

    def display(self, args):
        print(self.__current_list)
        if len(args) > 0:
            self.__view.output('display accepts no parameters')
        else:
            for row in self.__current_list:
                self.__view.output(', '.join(row.to_list()))

    def save_to_database(self, args):
        if len(args) > 0:
            self.__view.output('display accepts no parameters')
        elif self.__current_list is []:
            self.__view.output('No data to save')
        else:
            self.__iterate_data()

    def __iterate_data(self):
        for line in self.__current_list:
            # if the field doesn't exist insert
            if self.__database_view.select(self.__query_creator.get_emp_id_test(line[Employee.EMP_ID])) is None:
                self.__database_view.query(self.__query_creator.get_insert(line))
            else:
                self.__view.output("Line {} already exists in database".format(line[Employee.EMP_ID]))

    def get_from_database_for_view(self, args):
        data = self.__database_view.select(self.__query_creator.create_select(args))

        for i in data:
            self.__view.output(' '.join(i))

    def chart_pie(self, title, **kwargs):
        sql = ''
        if 'label' in kwargs:
            sql = self.__query_creator.get_pie_data_sum(kwargs['data'], kwargs['labels'])
        else:
            sql = self.__query_creator.get_pie_data_count(kwargs['data'])

        new_list = self.__get_chart_data(sql)
        data_x = 1  # list numbers
        label_x = 0
        self.__graph_view.plot_pie(title, new_list[label_x], new_list[data_x])

    def chart_bar(self, title, x, y, top):
        sql = self.__query_creator.get_bar_data(x, y, top)
        new_list = self.__get_chart_data(sql)
        x_pos = 0
        y_pos = 1
        self.__graph_view.plot_bar(title, self.__query_creator.LINE[x],
                                   self.__query_creator.LINE[y], new_list[x_pos], new_list[y_pos])

    def __get_chart_data(self, sql):
        from_db = self.__database_view.select(sql)
        return self.__fix_list(from_db)

    @staticmethod
    def __fix_list(from_db):
        new_list = [[], []]

        for i in from_db:
            new_list[0].append(i[0])
            new_list[1].append(i[1])

        return new_list
