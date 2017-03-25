# Created by Simon Winder

from .logger_base import Logger_Base
import json


class Logger(Logger_Base):

    def __init__(self):
        self.__load_config()

    def __load_config(self):
        with open('src\config.json') as json_data_file:
            data = json.load(json_data_file)['log']
            self.__file = data['file']

    def log_this(self, line, message):
        f = open(self.__file, 'w')
        f.writelines(["{}: {}".format(line, message)])
