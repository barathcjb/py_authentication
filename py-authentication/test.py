from handler import Client
import getpass


c = Client(auth_file_location='.')
c.addUsername(username="Barathwaj")
c.addPassword(password="Sholmes02-", length=(0, 16), hashAlgo="sha512")
c.addAttribute(attribute="age", value=22)
c.logCredents()
c.viewAuthDb()
print(c.validate(username="Barathwaj", password="Sholmes02-", algo='sha512'))
c.secureAuthData(dest_file_location='.',password='123')