import sys
import os
from src.controller.controller import Controller
from src.controller.view import View


def main():
    view = View()
    ctrl = Controller(view)
    view.inject_controller(ctrl)

    if len(sys.argv) > 1:
        view.onecmd(' '.join(sys.argv[1:]))
    view.cmdloop()

main()
