#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
setup.py
(c) Will Roberts  14 April, 2014

distutils setup script for pytimeparse.
'''

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import sys

with open('README.rst') as file:
    LONG_DESCRIPTION = file.read()

# http://stackoverflow.com/a/19719657/1062499
if sys.version_info[0] == 2:
    INSTALL_REQUIRES = ['future']
elif sys.version_info[0] == 3:
    INSTALL_REQUIRES = []

setup(name             = 'pytimeparse',
      version          = '1.1.0',
      description      = 'Time expression parser',
      author           = 'Will Roberts',
      author_email     = 'wildwilhelm@gmail.com',
      url              = 'https://github.com/wroberts/pytimeparse',
      packages         = ['pytimeparse'],
      license          = 'MIT',
      install_requires = INSTALL_REQUIRES,
      long_description = LONG_DESCRIPTION,
)
