'''
This file is made for testing the file IdentifyBaseWord in the model.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import IdentifyBaseWord as IdentifyBaseWord
import unittest

class IdentifyBaseWord_test (unittest.TestCase):
    
    # Initializes the class
    def setUp(self):
        self.base = IdentifyBaseWord
    
    # Tests automatic game functionality
    def test_autoGame(self):
        randUserLetters, randReqLetter = self.base.autoGame()
        self.assertTrue(randReqLetter.isalpha() and len(randReqLetter) == 1)
        self.assertTrue(randUserLetters.isalpha() and len(randUserLetters) == 7)
        
    
    # Tests base game functionality
    def test_baseGame(self):
        userInput = "pangrams"
        baseUserLetters, baseReqLetter = self.base.baseGame(userInput)
        self.assertTrue(baseReqLetter.isalpha() and len(baseReqLetter) == 1)
        self.assertTrue(baseUserLetters.isalpha() and len(baseUserLetters) == 7)
        
        userInput = "pangram"
        baseUserLetters, baseReqLetter = self.base.baseGame(userInput)
        print(baseReqLetter)
        print(baseUserLetters)
        self.assertEqual(baseReqLetter, "")
        self.assertEqual(baseUserLetters, "")

        userInpuyt = "abcdefghijklmnopqrstuvwxyz"
        baseUserLetters, baseReqLetter = self.base.baseGame(userInput)
        self.assertEqual(baseReqLetter, "")
        self.assertEqual(baseUserLetters, "")



if __name__ == '__main__':
    unittest.main()