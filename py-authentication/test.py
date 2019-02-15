#!usr/bin/env python3

__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'

from handler import Client

c = Client(auth_file_location='.')
# c.addUsername(username="Barathwaj")
# c.addPassword(password="Sholmes02-", length=(0, 16), hashAlgo="sha512")
# c.addAttribute(attribute="age", value=22)
# print(c._hashAlgo)
# c.logCredents()
# c.viewAuthFile()
# print(c.validate(username="Barathwaj", password="Sholmes02-", algo='sha512'))
c.unArchiveAuthData(dest_file_location='.', password='123')