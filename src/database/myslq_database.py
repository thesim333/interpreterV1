# Created by Simon Winder

from .database import Database
import sqlite3
from sqlite3 import Error


class DatabaseMySQL(Database):
    """
    Class for connecting with the mySQL db
    """

    __employee_sql = """
                    CREATE TABLE Employee(
                    EmpID VARCHAR(4) UNIQUE PRIMARY KEY,
                    Gender CHAR(1),
                    Age INT,
                    Sales INT,
                    BMI VARCHAR(11),
                    Salary INT,
                    DOB DATE);
                    """

    def __init__(self):
        Database.__init__(self)

    def _open(self):
        """
        Opens the db connection
        """
        self._connection = sqlite3.connect(self._database)
        self._session = self._connection.cursor()

        try:
            self._session.execute('SELECT * FROM Employee')
        except Error as e:
            if e == 'no such table: employee':
                self.query(self.__employee_sql)

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
        return_me = ""
        self._open()

        try:
            self._session.execute(sql)
            self._connection.commit()
            return_me = "Success"
        except Error as e:
            return_me = e
        self._close()
        return return_me

    def select(self, sql):
        """
        Preforms a sql select query and returns the result
        :param sql: the sql code for the query
        :return:
        """
        data = ""
        self._open()

        try:
            self._session.execute(sql)
            data = self._session.fetchall()
            self._connection.commit()
        except Error as e:
            data = e

        self._close()
        return data
