#!/usr/bin/env python

from distutils.core import setup

setup(name='bcp',
    version='0.1.5',
    url='https://github.com/adlibre/django-bcp',
    packages=['bcp',],
    install_requires=['django','reportlab',],
    package_data={ 'bcp': ['fonts/*', 'templates/*',] },
)
