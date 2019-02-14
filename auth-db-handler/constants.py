#!usr/bin/env python3

__author__ = 'Barathwaj C'
__email__ = 'barathcjb@gmail.com'


# password hash severity
NORMAL = 'NORMAL'
MEDIUM = 'MEDIUM'
STRONG = 'STRONG'

# supported algos

class MD4:
    def __init__(self):
        self.name = 'MD4'
        self.value = 0
class MD5:
    def __init__(self):
        self.name = 'MD5'
        self.value = 1
class SHA1:
    def __init__(self):
        self.name = 'SHA1'
        self.value = 2
class SHA224:
    def __init__(self):
        self.name = 'SHA224'
        self.value = 3

class SHA256:
    def __init__(self):
        self.name = 'SHA256'
        self.value = 4

class SHA384:
    def __init__(self):
        self.name = 'SHA384'
        self.value = 5

class SHA512:
    def __init__(self):
        self.name = 'SHA512'
        self.value = 6

algos = [MD4(),MD5(),SHA1(),SHA224(),SHA256(),SHA384(),SHA512()]