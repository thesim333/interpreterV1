# Created by Simon Winder

import cmd
import sys
from .view_base import ViewBase


class View(cmd.Cmd, ViewBase):
    def __init__(self):
        super().__init__()
        self.prompt = ">"

    def do_quit(self, args):
        """
        Exit the program
        """
        sys.exit()

    def do_load(self, args):
        """
        Loads employee information lines from a text file
        The data from this file will be validated
        All valid lines will be stored for use
        All lines with invalid data will be ignored and flagged on screen

        >load [path]
        """
        if len(args.split()) == 1:
            self._controller.load_file(args)
        else:
            self.output("Missing file path")

    def do_chart(self, args):
        """
        Begins the process for charting data from the database
        :param args: Bar or Pie
        """
        chart = ''
        if str.lower(args) == 'bar':
            chart = '1'
        elif str.lower(args) == 'pie':
            chart = '2'
        else:
            self.output("Type of chart")
            self.output("1 = Bar, 2 = Pie")
            chart = self.get_input("Number of option > ")

        if chart == '1':
            self.__chart_bar()
        elif chart == '2':
            self.__chart_pie()
        else:
            self.output("Invalid option")

    def __chart_pie(self):
        self.output("Which?:")
        self.output("1: Gender")
        self.output("2: BMI")
        self.output("3: Sales by Gender")
        self.output("4: Salary by Gender")
        self.output("5: Sales by BMI")
        self.output("6: Salary by BMI")
        decision = self.get_input("Select an option: ")
        if decision == '1':
            self._controller.chart_pie('Gender', 'Gender')
        elif decision == '2':
            self._controller.chart_pie('BMI', 'BMI')
        elif decision == '3':
            self._controller.chart_pie('Sales by Gender', 'Sales', 'Gender')
        elif decision == '4':
            self._controller.chart_pie('Salary by Gender', 'Salary', 'Gender')
        elif decision == '5':
            self._controller.chart_pie('Sales by BMI', 'Sales', 'BMI')
        elif decision == '6':
            self._controller.chart_pie('Salary by BMI', 'Salary', 'BMI')
        else:
            self.output("Invalid option")

    def __chart_bar(self):
        self.output("Which?:")
        self.output("1: Top 10 Sales")
        decision = self.get_input("Select an option: ")
        if decision == '1':
            self.__controller.chart_bar('Top 10 Sales', 'EmpID', 'Sales', 10)
        else:
            self.output("Invalid option")

    def do_save_to_database(self, args):
        """
        Saves the local data to the database
        Will not save duplicate employee id lines
        """
        self._controller.save_to_database(args)

    def do_pickle(self, args):
        """
        Pickles the currently loaded data to disk
        
        pickle [file] or default
        """
        self._controller.pickle(args.split())

    def do_unpickle(self, args):
        """
        Returns the pickled data from file
        
        unpickle [file] or default
        """
        self._controller.unpickle(args.split())

    @staticmethod
    def get_input(message):
        """
        Collects input from the user through the console
        :param message: Message to user asking for input
        :return: The input
        """
        return input(message + ':')

    def do_display(self, args):
        """
        Displays the current data to the console
        """
        self._controller.display(args)

    @staticmethod
    def __verify_db_input(the_input):
        if str.capitalize(the_input) == 'A':
            # all
            return '0,1,2,3,4,5,6'
        else:  # verify that all the numbers are numbers and in the valid range
            list_input = the_input.split(',')

            if list_input is []:
                return None

            list_input = set(list_input)  # remove duplicates

            try:
                int_list = list(map(int, list_input))
            except ValueError as e:
                return e

            int_list.sort()  # order id first date last

            if int_list[0] < 0 or int_list[-1] > 6:
                return None

            return ','.join(list(map(str, int_list)))
