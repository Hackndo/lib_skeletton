#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
from pip.req import parse_requirements
import os
import dummy

install_requirements = parse_requirements('requirements.txt',
                                          session=False)
requirements = [str(ir.req) for ir in install_requirements]
 
setup(
    name='dummy',
    version=dummy.__version__,
    packages=find_packages(),
    author="Hackndo",
    author_email="hackndo@gmail.com",
    description="IRC bot based on Sopel library",
    long_description=open('README.md').read(),
    install_requires= requirements,
    include_package_data=True,
    url='https://github.com/Hackndo/dummy',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: Eiffel Forum License, version 2",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: IRC",
    ],
    test_suite='tests',
    entry_points = {
        'console_scripts': [
            'dummy = dummy.core:run',
        ],
    },
)