#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='notifier',
    version='1.0',
    description='',
    author='Falaleev Maxim',
    author_email='max@studio107.ru',
    url='https://github.com/studio107/django-notifier',
    packages=find_packages(),
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
