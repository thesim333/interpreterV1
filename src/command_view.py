# written by Pippa Crawshaw

from view import View
from cmd import Cmd


# although command is a View from the VMC model and should not be able to
# call methods in the controller it is acceptable when using Cmd
# a controller in initialized in the constructor
# the set_controller is called from main
class CommandView(View, Cmd):
    # this presently uses View as a base class
    # but does not need any of the methods will need to look at this later
    def __init__(self):
        # calling the super class constructor
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_name = "unknown"
        self.controller = None

    # set the controller ready for calling methods
    def set_controller(self, controller):
        self.controller = controller

    def do_name(self, the_name):
        if the_name:
            self.my_name = the_name
        print(self.my_name)

    def do_file(self, the_name):
        """
        Syntax: file [the_name]
        :param the_name:
        :return:
        """
        if the_name:
            self.controller.show_all(the_name)
        print(the_name)

    def do_quit(self, line):
        """
        Syntax: quit
        :param line:
        :return:
        """
        print ("Quitting .......")
        return True

    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))

    # shortcuts
    do_q = do_quit

    def output(self, message):
        print('outputting')

    def get_input(self, prompt):
        print(prompt)
        return input()

    def start(self):
        print('MVC - the simplest example')

    def stop(self):
        print('Goodbye!')