# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class Database(metaclass=ABCMeta):
    """
    Abstract for Database Class
    """
    _instance = None
    _host = 'sql12.freemysqlhosting.net'
    _user = 'sql12163540'
    _password = 'LGj2eUHwim'
    _database = 'sql12163540'
    _session = None
    _connection = None

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
