#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
from pip.req import parse_requirements
import dummy

install_requirements = parse_requirements('requirements.txt',
                                          session=False)
requirements = [str(ir.req) for ir in install_requirements]
 
setup(
    name='dummy',
    version=dummy.__version__,
    packages=find_packages(),
    author="Hackndo",
    author_email="dummy@gmail.com",
    description="This is an awesome dummy thing",
    long_description=open('README.md').read(),
    install_requires= requirements,
    include_package_data=True,
    url='https://github.com/Hackndo/lib_skeleton',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: GPL",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: FooBar",
    ],
    test_suite='tests',
    entry_points = {
        'console_scripts': [
            'dummy = dummy.core:run',
        ],
    },
)
