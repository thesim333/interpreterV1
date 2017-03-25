# written by Pippa Crawshaw - March 2017
"""
input and output of a SQLite3 database
"""

from .data_view import View
import sqlite3
import json


class DatabaseView(View):
    _conn = object

    def get_input(self, database_file_name, sql):
        """
        Reads the database file and returns it as a list
        :param database_file_name:
        :param sql:
        :return:
        """
        database_as_list = []

        if not self.open_database(database_file_name):
            return

        # get all records
        cursor = self._conn.execute(sql)
        # put all the rows into a list
        database_as_list = cursor.fetchall()
        self.close_database()
        return database_as_list

    def open_database(self, database_file_name):
        """
        Opens the database
        :param database_file_name:
        """
        try:
            self._conn = sqlite3.connect(database_file_name)
        except Exception as e:
            print(e)
            return False
        else:
            print(database_file_name, "opened successfully")
            return True

    def close_database(self):
        """
        Closes the database
        """
        try:
            self._conn.close()
        except Exception as e:
            print(e)
        else:
            print("Closing database")

    def save_data_to_new(self, file_name, data_list):
        """
        Saves the data from <data_list> into a new database named <file_name>
        :param file_name:
        :param data_list:
        """
        if not self.open_database(file_name):
            return
        self.create_employee_table()
        self.insert_records(data_list)
        # commit the records before closing the database
        self._conn.commit()
        self.close_database()

    def create_employee_table(self):
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

    def insert_records(self, data_list):
        error_value = ''
        for i in data_list:
            try:
                self._conn.execute("INSERT INTO Employee "
                                   "VALUES (?,?,?,?,?,?,?)", i)
            except Exception as error_value:
                print(error_value)
            finally:
                print("Inserting record")
