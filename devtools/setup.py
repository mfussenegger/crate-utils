#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='cr8',
    version='0.1',
    entry_points={
        'console_scripts': [
            'cr8 = cr8:main',
        ]
    },
    py_modules=['cr8', 'timeit', 'json2insert'],
    install_requires=['crate', 'argh', 'requests']
)
