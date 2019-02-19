#!usr/bin/env python3

__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

import os
import marshal

import constants
import helper

__all__ = ['Client']


class Client:
    """
    Client API class to create functional userdata handling and manipulation
    by creating a light weight, portable authentication file.
    secure the data by zip archiving it with/without a password for the
    archive.

    Params:
     auth_file_location: path where the authentication file should be placed
    """

    def __init__(self, auth_file_location):
        self.__hashAlgo = None  # type: str
        self.__hash_value = None  # type:int
        self.__attribute = []
        self.__header = None  # type:str

        if os.path.isdir(auth_file_location):
            self.__file_location = os.path.abspath(
                auth_file_location) + "/authDB"

        else:
            raise Exception("invalid file location")

        self.__connection = None
        self.__loaded = None

    @property
    def _hashAlgo(self):
        return self.__hashAlgo

    @property
    def __hash_algo_value(self):
        for _obj in constants.algos:
            if _obj.name == self.__hashAlgo.upper():
                self.__hash_value = _obj.value
                break

        return self.__hash_value

    @property
    def __mergeDicts(self):
        userdata = {"header": self.__header,
                    "credents": {
                        "username": self.__username_obj.username,
                        "password": self.__password_obj._hash_password,
                        "algovalue": self.__hash_algo_value}
                    }
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
        try:
            self.__connection.close()
        except:
            pass

    def updateField(self, header, username, password,  attribute, value, hash_algo='md5'):
        """
        update the authentication file with specific configurations.

        Params:
         header: header is like table in sql
         username: username of the record
         password: password of the record
         hash_algo: if the administrator has used different algorithm for hashing
         value: new value to be updated in the attribute
        """
        self.__openConnection(mode='r')
        while True:
            try:
                self.__loaded = marshal.load(self.__connection)
                self.__connection.seek(0)
                __credents = self.__loaded
                __updater = helper.Updater(header=header,
                                           username=username,
                                           password=password,
                                           hash_algo=hash_algo,
                                           attribute=attribute,
                                           value=value,
                                           credents=__credents)
                if __updater.updateValue:
                    new_attribute, old_userdata = __updater.updateValue
                    self.addPassword(password=password, hashAlgo=hash_algo)
                    new_userdata = {"header": header,
                                    "credents": {
                                        "username": username,
                                        "password": self.__password_obj._hash_password,
                                        "algovalue": hash_algo}
                                    }
                    temp_data = new_userdata.copy()
                    temp_data.update(new_attribute)
                    self.__openConnection(mode='w')
                    marshal.dump(temp_data, self.__connection, 2)
                    self.__closeConnection()
                    break
            except EOFError:
                return False
                break

        self.__closeConnection()

    def addHeader(self, header):
        """
        add header to the userdata

        Params:
         header: header is like table in sql. Add header to segregate data.
        """
        self.__header = header

    def addUsername(self, username, hash_it=False, hash_algo='md5'):
        """
        create a username.

        Params:
         username: string of the desired username
         hash_it: boolean to specify if username should be hashed.(False by default)
         hash_algo: specify the hashing algorithm to hash the username.(md5 default)
        """
        self.__username_obj = helper.Username(hash_it)
        self.__username_obj.set_username(username=username)

    def addPassword(self, password='', length=(0, 32), hashAlgo='md5',
                    uppercase=True, specialchars=True, numbers=True, ignore=''):
        """
        create a password with various configureation to it.

        Params:
         password: password string that must be stored
         length: tuple containing minimum and maximum length of password string
         hashAlgo: hashing algorithm to be used (md5 by default)
         uppercase: boolean to specify if password can have uppercase characters
         specialchars: boolean to specify if password can have speical characters
         number: boolean to specify if password can have numbers
         ignore: comma separated string to specify characters to ignore in password
        """

        self.__hashAlgo = hashAlgo
        self.__password_obj = helper.Password(password=password, length=length, separator='_',
                                              hashAlgo=hashAlgo, uppercase=uppercase, specialchars=specialchars,
                                              numbers=numbers, ignore=ignore)

    def addAttribute(self, attribute, value):
        """
        add a new attribute to the particular userdata.
        call the function the number of times the number of attributes to be
        registered.

        Params:
         attribute: name of the attribute
         value: value of the attribute
        """
        self.__attribute.append((attribute, value))

    def logCredents(self):
        """
        store the configured userdata into the authentication file
        """
        # if self.__header == None:
        #     raise Exception('header of the userdata cannot be None')
        self.__openConnection(mode='w')
        marshal.dump(self.__mergeDicts, self.__connection, 2)
        self.__closeConnection()

    def viewAuthFile(self):
        """
        view the contents of the authentication file
        """
        self.__openConnection(mode='r')
        while True:
            try:
                self.__loaded = marshal.load(self.__connection)
                print(self.__loaded)
            except EOFError:
                break
        self.__closeConnection()

    def validate(self, header, username, password, algo='md5'):
        """
        validate a username and password with the authentication
        file. default hash algorithm if not mentioned by the user is md5.

        Params:
         username: username
         password: password
         algo: hash algorithm to be used if specified while creating userdata(md5 default)
        """
        self.__openConnection(mode='r')
        while True:
            try:
                self.__loaded = marshal.load(self.__connection)
                __credents = self.__loaded
                __validator = helper.Validator(header=header,
                                               username=username,
                                               password=password,
                                               algo=algo,
                                               credents=__credents)
                if __validator.validation:
                    return True
                    break
            except EOFError:
                return False
                break

        self.__closeConnection()

    def secureAuthData(self, dest_file_location, password):
        """
        archive authentication file as a zip file with password protection
        for shipping.

        Params:
         dest_file_location: destination path for archive file
         password = password for the archive file
        """
        self.__closeConnection()
        self.__security = helper.secureData(dest_file_location, password)
        self.__security._compress()

    def unArchiveAuthData(self, dest_file_location, password):
        """
        unarchive authentication file from a zip file with password protection
        for local usage.

        Params:
         dest_file_location: destination path of archive file
         password = password of the archive file
        """
        self.__closeConnection()
        self.__security = helper.secureData(dest_file_location, password)
        self.__security._decompress()
