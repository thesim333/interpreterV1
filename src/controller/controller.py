# Created by Simon Winder

import json
from src.text_file_reader.file_reader import FileReader
from src.database.myslq_database import DatabaseMySQL
from src.graph.graph import Graph
from src.serial.serial import Serial
from src.validator.employee import Employee


class Controller:
    __view = None
    __file_view = None
    __database_view = None
    __graph_view = None
    __current_list = None
    __serial_file = None

    def __init__(self, view):
        self.__view = view
        self.__file_view = FileReader()
        self.__database_view = DatabaseMySQL()
        self.__graph_view = Graph()
        with open('src\config.json') as json_data_file:
            self.__serial_file = json.load(json_data_file)['pickle']['file']

    def load_file(self, path):
        data = self.__file_view.get_file_data(path)

        if data == FileNotFoundError:
            self.__view.output(data)
        else:
            self.__validate_contents(data)

    def __validate_contents(self, content):
        list_of_employees = []
        for line in content:
            validation = Employee(line)
            if validation.employee_is_valid():
                list_of_employees.append(validation)
            else:
                self.__view.output(validation.get_invalid_flags())

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
        if len(args) > 0:
            return 'display accepts no parameters'
        else:
            for row in self.__current_list:
                self.__view.output(', '.join(row))
