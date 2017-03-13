# Created by Simon Winder

from .database import Database
import pymysql


class DatabaseMySQL(Database):
    def _open(self):
        self._connection = pymysql.connect(self._host, self._user, self._password, self._database)
        self._session = self._connection.cursor()

    def _close(self):
        self._session.close()
        self._connection.close()

    def query(self, sql):
        self._open()
        self._session.execute(sql)
        self._connection.commit()
        self._close()

    def select(self, sql):
        self._open()
        self._session.execute(sql)
        data = self._session.fetchall()
        self._connection.commit()
        self._close()
        return data
