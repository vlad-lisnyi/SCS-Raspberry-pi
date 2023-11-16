#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages


setup(name='SCS',
    version='1.0',
    description='SCS bus Library',
    author='Michele',
    author_email='',
    url='https://scsshield.altervista.org/',
    install_requires=['janus', 'asyncserial', 'asyncio_mqtt', 'tinydb', 'gmqtt', 'uvloop', 'tornado', 'paho-mqtt'],
    packages=find_packages(),
    python_requires='>=3.6, <4',
    )
