#!/usr/bin/env python

from setuptools import setup

setup(name='bcp',
    version='0.1.6',
    long_description=open('README.md').read(),
    url='https://github.com/adlibre/django-bcp',
    packages=['bcp',],
    install_requires=['django','reportlab',],
    package_data={ 'bcp': ['fonts/*', 'templates/*',] },
)
