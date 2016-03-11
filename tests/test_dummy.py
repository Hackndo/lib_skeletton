#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from dummy import dummy

class DummyTestCase(unittest.TestCase):

    def setUp(self):
        self.tobcri = dummy.Dummy()

    def test_true(self):
        self.assertEqual('Hello World!', str(self.tobcri))

if __name__ == '__main__':
    unittest.main()