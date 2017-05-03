# Created by Simon Winder

from abc import ABCMeta
from abc import abstractstaticmethod


class CreatorBase(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_pie_data_sum(self, data, labels):
        """Not Implemented"""

    @abstractstaticmethod
    def get_pie_data_count(self, data):
        """Not Implemented"""

    @abstractstaticmethod
    def get_bar_data(self, x, y, top):
        """Not Implemented"""
