# Created by Simon Winder

from .data_fixer_abc import DataFixerABC


class DataFixer(DataFixerABC):
    def __init__(self, the_old_list):
        super().__init__(the_old_list)

    def fix_the_list(self):
        for i in self._the_old_list:
            self._the_new_list[0].append(i[0])
            self._the_new_list[1].append(i[1])
