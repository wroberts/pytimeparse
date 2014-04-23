#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
setup.py
(c) Will Roberts  14 April, 2014

distutils setup script for pytimeparse.
'''

from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name             = 'pytimeparse',
      version          = '1.1.0',
      description      = 'Time expression parser',
      author           = 'Will Roberts',
      author_email     = 'wildwilhelm@gmail.com',
      url              = 'https://github.com/wroberts/pytimeparse',
      packages         = ['pytimeparse'],
      long_description = long_description,
)
