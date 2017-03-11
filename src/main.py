# written by Pippa Crawshaw

from controller import Controller
from model import Model
from command_view import CommandView
from csv_file_view import CsvFileView

#

if __name__ == "__main__":
    # running controller function
    cmd_view = CommandView()
    csv_view = CsvFileView()
    ctrl = Controller(csv_view, cmd_view, Model())
    # set the controller so cmd_view can call methods within the controller
    cmd_view.set_controller(ctrl)
    ctrl.start()
