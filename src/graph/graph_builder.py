# Created by Simon Winder

from abc import ABCMeta, abstractmethod
from .data_fixer import DataFixer


class GraphBuilder(metaclass=ABCMeta):
    def __init__(self, db_view, title):
        self._data = None
        self._label = None
        self._title = title
        self._db_view = db_view
        self._my_colors = 'rgbkymc'

    @abstractmethod
    def set_titles(self):
        pass

    @abstractmethod
    def create_chart_structure(self):
        pass

    def _fix_data(self, raw_data):
        data_fixer = DataFixer(raw_data)
        self._data = data_fixer.get_new_list_data()
        self._label = data_fixer.get_new_list_label()

    def _get_data_from_db(self, sql):
        self._fix_data(self._db_view.get_input(sql))

    @abstractmethod
    def get_data_for_chart(self):
        pass

    @abstractmethod
    def get_chart(self):
        pass
