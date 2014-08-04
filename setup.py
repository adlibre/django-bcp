#!/usr/bin/env python

from setuptools import setup

VERSION = '0.2.2'

setup(name='django-bcp',
    version=VERSION,
    author="Andrew Cutler",
    author_email="andrew@adlibre.com.au",
    description="Barcode Printer for Django",
    license="BSD",
    long_description=open('README.md').read(),
    url='https://github.com/adlibre/django-bcp',
    packages=['bcp',],
    download_url='https://github.com/adlibre/python-bureaucrat/archive/v%s.tar.gz' % VERSION,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    install_requires=[
    	'django', 
    	'reportlab==2.6', 
    ],
    package_data={'bcp': ['fonts/*', 'templates/*', ]},
)
