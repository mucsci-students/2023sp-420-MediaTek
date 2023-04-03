'''
This file is meant to test the functions in pangramdb.py.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import pangramdb as pangramdb
import unittest

# A new class for unittest to recognize.
class pangramdb_test (unittest.TestCase):
    
    # Set up unittest.
    def setUp(self):
        self.db = pangramdb
    
    # Test the random base function.
    def test_randomBase(self):
        testString = self.db.randomBase()
        self.assertTrue(testString.isalpha() and len(testString) > 0)