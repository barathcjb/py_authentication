#!usr/bin/env python3

""" Module to handle user API calls to database handling """

__project__ = "authentication database handler"
__version__ = '0.0.1'
__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

import os
import sqlite3 as sqlite
import crypt
import hashlib


class CreateDatabase(object):
    def __init__(self, database, timeout=20, password=None):
        self.connection = sqlite.connect(database=database, timeout=timeout)
        self.connection.set_authorizer
        self.cur = self.connection.cursor()
        self.table = []
        self.attributes = []
        if password != None:
            self.password = hashlib.sha3_256(password).hexdigest()
        self.cur.execute("PRAGMA key=%s"%(self.password))

    def createTable(table: str, attribute: tuple):
        self.attributes.append(attribute)
        self.table.append(table)
        self.cur.execute("create table %s %s" % (table, attribute))

    def viewDatabase():
        db_views = []
        for (table, _attri) in zip(self.table, self.attributes):
            db_views.append((table, _attri))
        return db_views

    def viewTable(table: str, conditions: str):
        table_views = []
        rows = self.cur.execute("select * from %s %s" % (table, conditions))
        for _items in rows:
            table_views.append(_items)
        return table_views

    def viewRow(table: str, attribute: tuple, conditions: str):
        select_rows = []
        rows = self.cur.execute('select %s from %s where %s' %
                                (table, attribute, conditions))
        for _items in rows:
            select_rows.append(_items)
        return select_rows
