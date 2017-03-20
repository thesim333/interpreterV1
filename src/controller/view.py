# Created by Simon Winder

import cmd
import sys


class View(cmd.Cmd):
    __controller = None
    prompt = ">"

    def inject_controller(self, ctrl):
        self.__controller = ctrl

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
        self.__controller.load_file(args)

    def do_graph(self, args):
        """

        :param args:
        :return:
        """
        print(args.split())

    def do_to_database(self, args):
        """

        :param args:
        :return:
        """
        pass

    def do_from_db(self, args):
        """

        :param args:
        :return:
        """
        pass

    @staticmethod
    def output(message):
        """

        :param message:
        :return:
        """
        print(message)

    def do_pickle(self, args):
        """
        Pickles the currently loaded data to disk
        """
        self.__controller.pickle(args.split())

    def do_unpickle(self, args):
        """
        Returns the pickled data from file
        Options [overwrite : append] overwrite is default
        """
        self.__controller.unpickle(args.split())

    @staticmethod
    def get_input(message):
        """

        :param message:
        :return:
        """
        return input(message + ':')

    def do_display(self, args):
        """

        :param args:
        :return:
        """
        self.__controller.display(args)
