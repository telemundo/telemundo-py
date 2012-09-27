#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='TelemundoPy',
    version='0.1-dev',
    url='https://github.com/telemundo/telemundo-py',
    author='Rodolfo Puig',
    author_email='rodolfo.puig@nbcuni.com',
    description='Telemundo Python Libraries',
    keywords='Telemundo',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    platforms='any'
)
