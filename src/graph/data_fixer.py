# Created by Simon Winder

from .data_fixer_abc import DataFixerABC


class DataFixer(DataFixerABC):
    """
    Class that rearranges database query list
    """
    def __init__(self, the_old_list):
        super().__init__(the_old_list)

    def fix_the_list(self):
        """
        separates the label and data portions of the list from the database
        """
        for i in self._the_old_list:
            self._labels.append(i[0])
            self._data.append(i[1])
