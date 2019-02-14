#!usr/bin/env python3

__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

import string
import hashlib
import random
import constants

__all__ = ['Username', 'Password']


class Username:
    def __init__(self,hash_it):
        self._username = None
        self.is_hash = hash_it

    def set_username(self, username, hashAlgo='md5'):
        self._username = username
        self._hashAlgo = hashAlgo
        self._hashed_username = self._username

    @property
    def username(self):
        if self.is_hash:
            self._hashed_username = getattr(hashlib, self._hashAlgo)(
                self._username.encode('utf-8')).hexdigest()
        return self._hashed_username


class Password:
    def __init__(self, password='', length=(0, 32), separator='_',
                 hashAlgo='md5', uppercase=False, specialchars=True, numbers=True, ignore=''):
        self._minimum_chars = length[0]
        self._maximum_chars = length[1]
        self._separator = separator
        self._special_chars = specialchars
        self._hash = hashAlgo
        self._uppercase = uppercase
        self._number = numbers
        self._ignore_list = ignore.split(',')
        self._password = self._build_password(password)
        self._hash_value = self.determineAlgo

    @property
    def _hash_password(self):
        # if self._hash in list(hashlib.algorithms_available):
        self._hashed_password = getattr(hashlib, self._hash)(
            self._password.encode('utf-8')).hexdigest()
        # else:
        #     raise exceptions.algoNotFountException()
        return self._hashed_password

    @property
    def determineAlgo(self):
        for _obj in constants.algos:
            if _obj.name == self._hash.upper():
                _hash_value = _obj.value
                break
                return _hash_value

    def _build_password(self, password: str):
        if password == '':
            _chars = string.ascii_lowercase
            if self._uppercase:
                _chars += string.ascii_uppercase
            if self._special_chars:
                _chars += string.punctuation
            if self._number:
                _chars += string.digits

            for ignore_key in _chars:
                if ignore_key in self._ignore_list:
                    _chars.replace(ignore_key, '')

            _chars = '{message:{fill}{align}{width}}'.format(
                message=_chars,
                fill='0',
                align='>',
                width=self._maximum_chars,
            )

            return ''.join([random.choice(_chars)for i in range(
                self._minimum_chars, self._maximum_chars)])
        else:
            return password


class Validator:
    def __init__(self, username, password, algo, credents):
        self._username = username
        self._password = password
        self._algo = algo
        self._fp_username = credents[0]
        self._fp_password = credents[1]
        self._fp_algo = credents[3]

    @property
    def validation(self):
        if self._username == self._fp_username and getattr(hashlib, self._algo)(
                self._password.encode('utf-8')).hexdigest() == self._fp_password:
            return True
        return False
