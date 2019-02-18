#!usr/bin/env python3

__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

import string
import hashlib
import os
import random
import constants
import pyminizip


class Username:
    def __init__(self, hash_it, hashAlgo='md5'):
        self.__username = None
        self.__is_hash = hash_it
        self.__hashAlgo = hashAlgo
        self.__hashed_username = None

    def set_username(self, username):
        self.__username = username
        self.__hashed_username = self.__username

    @property
    def username(self):
        if self.__is_hash:
            self.__hashed_username = getattr(hashlib, self.__hashAlgo)(
                self.__username.encode('utf-8')).hexdigest()
        return self.__hashed_username


class Password:
    def __init__(self, password='', length=(0, 32), separator='_',
                 hashAlgo='md5', uppercase=False, specialchars=True, numbers=True, ignore=''):
        self.__minimum_chars = length[0]
        self.__maximum_chars = length[1]
        self.__separator = separator
        self.__special_chars = specialchars
        self.__hash = hashAlgo
        self.__uppercase = uppercase
        self.__number = numbers
        self.__ignore_list = ignore.split(',')
        self.__password = self.__build_password(password)
        self.__hash_value = self.__determineAlgo

    @property
    def _hash_password(self):
        # if self.__hash in list(hashlib.algorithms_available):
        self._hashed_password = getattr(hashlib, self.__hash)(
            self.__password.encode('utf-8')).hexdigest()
        # else:
        #     raise exceptions.algoNotFountException()
        return self._hashed_password

    @property
    def __determineAlgo(self):
        for _obj in constants.algos:
            if _obj.name == self.__hash.upper():
                __hash_value = _obj.value
                break
                return __hash_value

    def __build_password(self, password: str):
        if password == '':
            __chars = string.ascii_lowercase
            if self.__uppercase:
                __chars += string.ascii_uppercase
            if self.__special_chars:
                __chars += string.punctuation
            if self.__number:
                __chars += string.digits

            for ignore_key in __chars:
                if ignore_key in self.__ignore_list:
                    __chars.replace(ignore_key, '')

            __chars = '{message:{fill}{align}{width}}'.format(
                message=__chars,
                fill='0',
                align='>',
                width=self.__maximum_chars,
            )

            return ''.join([random.choice(__chars)for i in range(
                self.__minimum_chars, self.__maximum_chars)])
        else:
            return password


class Validator:
    def __init__(self, header, username, password, algo, credents):
        self.__header = header
        self.__username = username
        self.__password = password
        self.__algo = algo
        self.__fp_header = credents['header']
        self.__fp_username = credents['username']
        self.__fp_password = credents['password']
        self.__fp_algo = credents['algovalue']

    @property
    def validation(self):
        if self.__header == self.__fp_header and self.__username == self.__fp_username and getattr(hashlib, self.__algo)(
                self.__password.encode('utf-8')).hexdigest() == self.__fp_password:
            return True
        return False


class Updater:
    def __init__(self, header, username, password, hash_algo, attribute, value, credents):
        self.__attribute = attribute
        self.__value = value
        self.__credents = credents
        self.__validator = Validator(
            header, username, password, hash_algo, credents)

        if attribute not in credents.keys():
            raise AttributeError('mentioned attribute not present')
        if attribute == 'password':
            raise Exception('passwords cannot be changed')

    @property
    def updateValue(self):
        if self.__validator.validation:
            return {self.__attribute: self.__value}, self.__credents


class secureData:
    def __init__(self, file_location, password):
        self.__auth_file = os.path.abspath(file_location)+"/authDB"
        self.__password = password
        self.__zip_path = self.__auth_file + ".zip"

    def _compress(self):
        data = pyminizip.compress(
            self.__auth_file, None, self.__auth_file+".zip", self.__password, 5)

    def _decompress(self):
        data = pyminizip.uncompress(
            self.__zip_path, self.__password, os.path.abspath(os.path.dirname(self.__auth_file)), 0)
