# Created by Simon Winder

from abc import ABCMeta
from abc import abstractmethod


class ValidateField(metaclass=ABCMeta):
    _valid = "Valid"

    def __init__(self, field):
        self.field = field

    @abstractmethod
    def validate(self):
        pass
