#!usr/bin/env python3

__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

import os
import marshal

import constants
import helper

__all__ = ['Client', 'Username', 'Password']


class Client:
    def __init__(self, auth_file_location):
        self.__hashAlgo = None  # type: str
        self.__hash_value = None  # type:int
        self.__attribute = []

        if os.path.isdir(auth_file_location):
            self.__file_location = auth_file_location + "authDB"
        else:
            raise Exception("invalid file location")

        self.__connection = None
        self.__cursor = None
        self.__loader = None

    @property
    def __hash_algo_value(self):
        for _obj in constants.algos:
            if _obj.name == self.__hashAlgo.upper():
                self.__hash_value = _obj.value
                break

        return self.__hash_value

    @property
    def __mergeDicts(self):
        userdata = {"username": self.__username_obj.username,
                    "password": self.__password_obj._hash_password,
                    "algovalue": self.__hash_algo_value}
        if self.__attribute.__len__() != 0:
            temp_data = userdata.copy()
            temp_data.update(dict(self.__attribute))
            return temp_data
        return userdata

    def __openConnection(self, mode):
        if mode == 'w':
            self.__connection = open(self.__file_location, 'ab+')
        if mode == 'r':
            self.__connection = open(self.__file_location, 'rb+')

    def __closeConnection(self):
        self.__connection.close()

    def addUsername(self, username, hash_it=False, hash_algo='md5'):
        self.__username_obj = helper.Username(hash_it)
        self.__username_obj.set_username(username=username)

    def addPassword(self, password='', length=(0, 32), separator='_',
                    hashAlgo='md5', uppercase=True, specialchars=True, numbers=True, ignore=''):
        self.__hashAlgo = hashAlgo
        self.__password_obj = helper.Password(password=password, length=length, separator=separator,
                                              hashAlgo=hashAlgo, uppercase=uppercase, specialchars=specialchars,
                                              numbers=numbers, ignore=ignore)

    def addAttribute(self, attribute, value):
        self.__attribute.append((attribute, value))

    def logCredents(self):
        self.__openConnection(mode='w')
        marshal.dump(self.__mergeDicts, self.__connection, 2)
        self.__closeConnection()

    def viewAuthDb(self):
        self.__openConnection(mode='r')
        while True:
            try:
                self.__loaded = marshal.load(self.__connection)
                print(self.__loaded)
            except EOFError:
                break
        self.__closeConnection()

    def validate(self, username, password, algo='md5'):
        self.__openConnection(mode='r')
        # self.__loader = pickle.Unpickler(self.__connection)
        __validation = False
        while True:
            try:
                self.__loaded = marshal.load(self.__connection)
                _credents = self.__loaded
                __validator = helper.Validator(
                    username, password, algo, _credents)
                if __validator.validation:
                    return True
                    break
            except EOFError:
                return False
                break
        self.__closeConnection()

    def secureAuthData(self, dest_file_location, password):
        self.__connection.close()
        self.__security = helper.secureData(dest_file_location, password)
        self.__security._compress()
