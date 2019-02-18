user authentication handler library for python. Uses password hashing and user data storage for user input authentication paramerters with user data validation API.

pure pythonic library to store, manipulate and retrieve usernames and passwords into new/existing sophisticated datafile


example usage:

from pyauthentication.handler import Client

obj = Client(auth_file_location='.')
obj.addUsername(username="Barathwaj")
obj.addPassword(password="123", length=(0, 16), hashAlgo="sha512")
obj.addAttribute(attribute="age", value=22)
obj.logCredents()
obj.viewAuthFile()
print(obj.validate(username="Barathwaj", password="123-", algo='sha512'))
obj.unArchiveAuthData(dest_file_location='.', password='123')