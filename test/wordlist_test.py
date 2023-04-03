'''
This file is meant to test the functions in wordlist.py.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import wordlist as wordlist
import unittest

class wordlist_test (unittest.TestCase):
    
    # Set up unittest
    def setUp(self):
        self.wl = wordlist
    
    # Test word list generation
    def test_generateWordList(self):
        
        # Create a required letter and user letters
        self.reqLetter = "o"
        self.userLetters = "mediocr"
        
        # Generate a new word list
        self.wordlist = self.wl.generateWordList(self.reqLetter, self.userLetters)
        
        # Ensure a word list is generated by checking the length, the middle and both extremes of the list.
        self.assertGreater(len(self.wordlist), 0)
        self.assertTrue(self.wordlist.__contains__("mediocre"))
        self.assertTrue(self.wordlist.__contains__("cero"))
        self.assertTrue(self.wordlist.__contains__("rerecorded"))
    
    # Tests the checkLetters function
    def test_checkLetters(self):
        
        # Use a valid pangram
        self.letters = "mediocr"
        
        # Test a small letter that fits.
        self.wordOne = "dice"
        self.testOne = self.wl.checkLetters(self.wordOne, self.letters)
        self.assertEqual(self.testOne, 0)
        
        # Tests a medium letter that fits.
        self.wordTwo = "record"
        self.testTwo = self.wl.checkLetters(self.wordTwo, self.letters)
        self.assertEqual(self.testTwo, 0)
        
        # Test a large letter that does fit.
        self.wordThree = "reordered"
        self.testThree = self.wl.checkLetters(self.wordThree, self.letters)
        self.assertEqual(self.testThree, 0)
        
        # Test one or two letters out of place.
        self.wordFour = "microbots"
        self.testFour = self.wl.checkLetters(self.wordFour, self.letters)
        self.assertGreater(self.testFour, 0)
        
        # Test a new more letters out of place.
        self.wordFive = "deals"
        self.testFive = self.wl.checkLetters(self.wordFive, self.letters)
        self.assertGreater(self.testFive, 0)
        
        # Test all letters out of place.
        self.wordSix = "neat"
        self.testSix = self.wl.checkLetters(self.wordSix, self.letters)
        self.assertGreater(self.testSix, 0)
        
        