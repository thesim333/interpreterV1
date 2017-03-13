# Created by Simon Winder

from .serial_base import SerialBase
import pickle


class Serial(SerialBase):
    @classmethod
    def pickle_this(cls, file, content):
        try:
            file_object = open(file, 'wb')
            pickle.dump(content, file_object)
            file_object.close()
        except IOError:
            return 'Could not write to file {}'.format(file)

    @classmethod
    def unpickle_this(cls, file):
        try:
            file_object = open(file, 'rb')
            content = pickle.load(file_object)
            file_object.close()
            return content
        except FileNotFoundError:
            return 'Could not open {}'.format(file)
