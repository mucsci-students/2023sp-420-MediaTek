'''
This file is meant to test the functions in wordstuff.py.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import wordstuff as wordstuff
import unittest


class wordstuff_test (unittest.TestCase):
    
    # Sets up unittest
    def setUp(self):
        self.ws = wordstuff
    
    # Tests the checkword function.
    def test_checkWord(self):
        
        # Test one: short word
        wordOne = "word"
        testOne = self.ws.checkWord(wordOne)
        self.assertTrue(testOne)
        
        # Test two: long word
        wordTwo = "availability"
        testTwo = self.ws.checkWord(wordTwo)
        self.assertTrue(testTwo)
        
        # Test three: not an actual word
        wordThree = "notanactualword"
        testThree = self.ws.checkWord(wordThree)
        self.assertFalse(testThree)
        
        # Test four: ?????
        wordFour = "ewioefwisf"
        testFour = self.ws.checkWord(wordFour)
        self.assertFalse(testFour)