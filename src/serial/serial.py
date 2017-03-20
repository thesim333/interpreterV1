# Created by Simon Winder

from .serial_base import SerialBase
import pickle


class Serial(SerialBase):
    """
    Class that preforms the pickle and unpickle actions
    """
    @classmethod
    def pickle_this(cls, file, content):
        """
        Pickles data to a file for later retrieval
        :param file: Where to write
        :param content: Stuff to pickle
        :return: An error if write could not be preformed
        """
        try:
            file_object = open(file, 'wb')
            pickle.dump(content, file_object)
            file_object.close()
        except IOError:
            return 'Could not write to file {}'.format(file)

    @classmethod
    def unpickle_this(cls, file):
        """
        Retrieves the data from the file
        :param file: The file
        :return: The data from the file
        """
        try:
            file_object = open(file, 'rb')
            content = pickle.load(file_object)
            file_object.close()
            return content
        except FileNotFoundError as e:
            return e
