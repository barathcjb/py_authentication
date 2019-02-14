#!usr/bin/env python3

__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

import gnupg
import os
import pickle

import constants
import helper

__all__ = ['Client', 'Username', 'Password']


class Client:
    def __init__(self, auth_file_location):
        self._hashAlgo = None  # type: str
        self._hash_value = None  # type:int
        self._remarks = ''

        if os.path.isdir(auth_file_location):
            self._file_location = auth_file_location
        else:
            raise Exception("invalid file location")

        self._connection = None
        self._cursor = None
        self._loader = None

    @property
    def hash_value(self):
        for _obj in constants.algos:
            if _obj.name == self._hashAlgo.upper():
                self._hash_value = _obj.value
                break

        return self._hash_value

    def _openConnection(self, mode):
        if mode == 'w':
            self._connection = open(os.path.join(
                self._file_location, 'authDb'), 'ab')
        if mode == 'r':
            self._connection = open(os.path.join(
                self._file_location, 'authDb'), 'rb')

    def _closeConnection(self):
        self._connection.close()

    def addUsername(self, username, hash_it=False):
        self._username_obj = helper.Username(hash_it)
        self._username_obj.set_username(username=username)

    def addPassword(self, password='', length=(0, 32), separator='_',
                    hashAlgo='md5', uppercase=True, specialchars=True, numbers=True, ignore=''):
        self._hashAlgo = hashAlgo
        self._password_obj = helper.Password(password=password, length=length, separator=separator,
                                             hashAlgo=hashAlgo, uppercase=uppercase, specialchars=specialchars,
                                             numbers=numbers, ignore=ignore)

    def addRemarks(self, remarks):
        self._remarks = remarks

    def logCredents(self):
        self._openConnection(mode='w')
        self._cursor = pickle.Pickler(self._connection)
        print(self._username_obj.username)
        print(self._password_obj._hash_password)
        self._cursor.dump([self._username_obj.username,self._password_obj._hash_password, self._remarks, self.hash_value])
        self._closeConnection()

    def viewAuthDb(self):
        self._openConnection(mode='r')
        self._loader = pickle.Unpickler(self._connection)
        while True:
            try:
                print(self._loader.load())
            except EOFError:
                break
        self._closeConnection()

    def validate(self, username, password, algo='md5'):
        self._openConnection(mode='r')
        self._loader = pickle.Unpickler(self._connection)
        validation = False
        while True:
            try:
                _credents = self._loader.load()
                validator = helper.Validator(
                    username, password, algo, _credents)
                if validator.validation:
                    return True
                    break
            except EOFError:
                return False
                break
        self._closeConnection()


if __name__ == "__main__":
    c = Client(auth_file_location=os.path.dirname(__file__))
    c.addUsername(username="Barathwaj", hash_it=False)
    c.addPassword(hashAlgo='md5')
    c.addRemarks(remarks="hello world")
    c.logCredents()
    c.viewAuthDb()
    print(c.validate(username="Sholmes", password=""))
