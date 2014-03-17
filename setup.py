#!/usr/bin/env python

from setuptools import setup

setup(name='django-bcp',
    version='0.1.9',
    long_description=open('README.md').read(),
    url='https://github.com/adlibre/django-bcp',
    packages=['bcp',],
    install_requires=[
    	'django', 
    	'reportlab==2.6', 
    ],
    package_data={'bcp': ['fonts/*', 'templates/*', ]},
)
