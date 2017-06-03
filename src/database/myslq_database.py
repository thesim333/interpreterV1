# written by Pippa Crawshaw - March 2017
"""
input and output of a SQLite3 database
"""

from .data_view import DatabaseViewBase
import sqlite3


class DatabaseView(DatabaseViewBase):
    def __init__(self, database):
        super().__init__(database)

    def get_input(self, sql):
        """
        Reads the database file and returns it as a list
        :param sql:
        :return:
        """
        database_as_list = []

        if not self._open_database():
            return

        # get all records
        cursor = self._conn.execute(sql)
        # put all the rows into a list
        database_as_list = cursor.fetchall()
        self._close_database()
        return database_as_list

    def _open_database(self):
        """
        Opens the database
        """
        try:
            self._conn = sqlite3.connect(self._database)
        except Exception as e:
            print(e)
            return False
        else:
            print(self._database, "opened successfully")
            return True

    def _close_database(self):
        """
        Closes the database
        """
        try:
            self._conn.close()
        except Exception as e:
            print(e)
        else:
            print("Closing database")

    def save_data_to_new(self, data_list):
        """
        Saves the data from <data_list> into a new database named <file_name>
        :param data_list:
        """
        if not self._open_database():
            return
        self._create_employee_table()
        self._insert_records(data_list)
        # commit the records before closing the database
        self._conn.commit()
        self._close_database()

    def _create_employee_table(self):
        """
        Create the employee table in the previously opened database file
        """
        try:
            self._conn.execute('''CREATE TABLE IF NOT EXISTS Employee (
                EMPID      VarChar (4) primary key,
                Gender     VarChar (1),
                Age        int(2),
                Sales      int(3),
                BMI        VarChar(11),
                Salary     int(3),
                DOB   date);''')
        except Exception as e:
            print(e)
        else:
            print("Created table")

    def _insert_records(self, data_list):
        error_value = ''
        for i in data_list:
            try:
                self._conn.execute("INSERT INTO Employee "
                                   "VALUES (?,?,?,?,?,?,?)", i)
            except Exception as error_value:
                print(error_value)
            finally:
                print("Inserting record")
