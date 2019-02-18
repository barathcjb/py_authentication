"""
Setup file.
"""
try:
    from setuptools import find_packages, setup
except:
    print('setuptools not found \n install python setup tools')

with open("README.md", "r") as readme:
    LONG_DESCRIPTION = readme.read()


AUTHOR = 'Barathwaj C'
AUTHOR_EMAIL = 'barathcjb@gmail.com'
DESCRIPTION = 'python module for secure userdata storage/manipulation/retrival/validation and cross platform usage'
VERSION = '1.0.0'
PACKAGE_NAME = 'py_authentication'
URL = 'https://github.com/barathcjb/py-authentication.git'
ADDITIONAL_INFO = dict(classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License'
]
)
INSTALL_REQUIRES = [
    'pyminizip'
],
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(exclude=['contrib', 'docs', 'tests', 'bin']),
      install_requires=INSTALL_REQUIRES,
      **ADDITIONAL_INFO
      )
