from handler import Client

obj = Client(auth_file_location='.')
obj.addHeader(header='sample')
obj.addUsername(username="Barathwaj")
obj.addPassword(password="123", length=(0, 16), hashAlgo="sha512")
obj.addAttribute(attribute="age", value=22)
obj.logCredents()
#print(obj.validate(header='sample',username="Barathwaj", password="123-", algo='sha512'))
#obj.unArchiveAuthData(dest_file_location='.', password='123')
#obj.updateField(header='sample',username='Barathwaj',password='123-',hash_algo='sha512',attribute='username',value='barath')
obj.viewAuthFile()
