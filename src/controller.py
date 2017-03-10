# Written by Pippa Crawshaw
from sys import argv


class Controller:
    # the views will be sent as a list of views
    # but at present are sent individually
    def __init__(self, csv_view, command_view, model):
        self.csv_view = csv_view
        self.command_view = command_view
        self.model = model

    def show_all(self, file_name):
        # gets list of all Data objects
        # data_in_csv = self.csv_view.get_input('db.csv')
        data_in_csv = self.csv_view.get_input(file_name)
        # calls view to output data in the csv file
        return self.csv_view.output(data_in_csv)

    def start(self):
        if len(argv) > 1:
            self.command_view.onecmd(' '.join(argv[1:]))
        else:
            self.command_view.cmdloop()
        # self.command_view.start()
        # my_input = self.command_view.get_input(
        #     'Do you want to see everyone in my db?[y/n]')
        # if my_input == 'y':
        #     return self.show_all()
        # else:
        #     return self.command_view.stop()
