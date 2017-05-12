#!/usr/bin/env python
# -*- coding: utf-8 -*-

PROJECT = 'airodump-iv'

VERSION = '0.2'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='A python implementation of airodump-ng',
    long_description=long_description,

    author='Ivan Leichtling',

    classifiers=['Development Status :: 3 - Alpha',
                 'Programming Language :: Python :: 2.7',
                 'Environment :: Console',
                 ],

    scripts=[],

    provides=[],
    install_requires=['scapy'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'airoiv = airoiv.airodump_iv:main'
        ],
    },

    zip_safe=False,
)
