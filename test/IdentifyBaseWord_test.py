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

class IdentifyBaseWord_test:
    
    # Initializes the class
    def __init__(self):
        self.base = IdentifyBaseWord
    
    # Tests automatic game functionality
    def autoGame_test(self):
        randUserLetters, randReqLetter = self.base.autoGame()
        assert (randReqLetter.isalpha()) and (len(randReqLetter) == 1)
        assert (randUserLetters.isalpha()) and (len(randUserLetters) == 7)
        
    
    # Tests base game functionality
    def baseGame_test(self):
        userInput = "pangrams"
        baseUserLetters, baseReqLetter = self.base.baseGame(userInput)
        assert (baseReqLetter.isalpha()) and (len(baseReqLetter) == 1)
        assert (baseUserLetters.isalpha()) and (len(baseUserLetters) == 7)
        
        userInput = "pangram"
        baseUserLetters, baseReqLetter = self.base.baseGame(userInput)
        print(baseReqLetter)
        print(baseUserLetters)
        assert len(baseReqLetter) == 0
        assert len(baseUserLetters) == 0