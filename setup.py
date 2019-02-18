"""
Setup file.
"""
try:
    from distutils.core import setup
except:
    print('setuptools not found \n install python setup tools')

with open("README.md", "r") as readme:
    LONG_DESCRIPTION = readme.read()


AUTHOR = 'Barathwaj C'
AUTHOR_EMAIL = 'barathcjb@gmail.com'
DESCRIPTION = 'python module for secure userdata storage/manipulation/retrival/validation \
     and cross platform usage of generated authentication file'
VERSION = '1.0.0'
LICENSE = 'MIT'
PACKAGE_NAME = 'pyauthentication'
URL = 'https://github.com/barathcjb/py_authentication.git'
ADDITIONAL_INFO = dict(classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]
)
INSTALL_REQUIRES = [
    'pyminizip'
]

REQUIRES = ['os','hashlib','sys','marshal']
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      install_requires=INSTALL_REQUIRES,
      packages=['pyauthentication'],
      license=LICENSE,
      scripts=['pyauthentication/handler.py'],
      requires=REQUIRES,
      include_package_data=True,
      zip_safe=False,
      **ADDITIONAL_INFO
      )
