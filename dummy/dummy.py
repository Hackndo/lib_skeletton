#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dummy():
    def __init__(self):
        self.foo = "Hello World!"

    def __str__(self):
        return self.foo

    def run(self):
        pass