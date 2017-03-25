# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod
import json


class Database(metaclass=ABCMeta):
    """
    Abstract for Database Class
    """
    _instance = None
    _host = None
    _user = None
    _password = None
    _database = None
    _session = None
    _connection = None

    def __init__(self):
        self.__load_config()

    def __load_config(self):
        with open('src\config.json') as json_data_file:
            data = json.load(json_data_file)['mysql']
            # self._host = data['host']
            # self._user = data['user']
            # self._password = data['passwd']
            self._database = data['db']

    @abstractmethod
    def _open(self):
        pass

    @abstractmethod
    def _close(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    @abstractmethod
    def select(self, sql):
        pass
