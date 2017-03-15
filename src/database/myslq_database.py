# Created by Simon Winder

from .database import Database
import pymysql


class DatabaseMySQL(Database):
    """
    Class for connecting with the mySQL db
    """
    def _open(self):
        """
        Opens the db connection
        """
        self._connection = pymysql.connect(self._host, self._user, self._password, self._database)
        self._session = self._connection.cursor()

    def _close(self):
        """
        Closes the db connection
        """
        self._session.close()
        self._connection.close()

    def query(self, sql):
        """
        Preforms a sql query that does not expect a return value
        :param sql: the sql code for the query
        """
        self._open()
        self._session.execute(sql)
        self._connection.commit()
        self._close()

    def select(self, sql):
        """
        Preforms a sql select query and returns the result
        :param sql: the sql code for the query
        :return:
        """
        self._open()
        self._session.execute(sql)
        data = self._session.fetchall()
        self._connection.commit()
        self._close()
        return data
