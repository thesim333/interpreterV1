# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class AgeValidate(metaclass=ABCMeta):
    @abstractmethod
    def check_age_against_date(self, age):
        pass
