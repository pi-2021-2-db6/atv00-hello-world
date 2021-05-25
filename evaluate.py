#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
*** DO NOT EDIT THIS FILE !!! ****
Test code for atv00

@author: Diogo S. Martins
"""

import unittest
import main

class Test(unittest.TestCase):
    def test_hello(self):
        self.assertEqual("Hello World!", main.say_hello(), 
                         "Message is different from expected")
        
if __name__ == '__main__':
    unittest.main()

