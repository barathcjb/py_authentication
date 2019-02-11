#!usr/bin/env python3

""" Module to handle user API calls to database handling """

__project__ = "authentication database handler"
__version__ = '0.0.1'
__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

import os
import sqlite3 as sqlite


class CreateDatabase(sqlite.Connection):
    def __init__(self):
        sqlite.Connection.__init__(self, **args)
        self._cur = self.cursor()
        self._table = []
        self._attributes = []

    def createTable(table: str, attribute: tuple):
        self._attributes.append(attribute)
        self._table.append(table)
        self._cur.execute("create table %s %s" % (table, attribute))

    def viewDatabase():
        dbviews = []
        for (_table, _attri) in zip(self._table, self._attributes):
            dbviews.append((_table, _attri))
        dbviews.clear()
        return dbviews

    def viewTable(table: str, conditions: str):
        self._cur.execute("select * from %s %s" % (table, conditions))
