'''
This file is made for testing the file savegame in the model.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import savegame as savegame
from MVC.model import wordlist as wordlist
import unittest
import json

class savegame_test (unittest.TestCase):
    
    # Initializes the class
    def setUp(self):
        self.wordlist = wordlist
    
    # Tests the savegame file for functionality
    def test_savegame(self):
        userLetters = "pangrms"
        reqLetter = "a"
        guessedWords = ["pangram", "pangrams", "grams", "gram"]
        wordList = wordlist.generateWordList(reqLetter, userLetters)
        points = 20
        maxPoints = 100
        
        # Unsure if this is the optimal way to test this but it's all I got with the knowlege I have.
        savegame(reqLetter, userLetters, points, maxPoints, guessedWords, wordList, "pangram")
        with open("pangram.json", "r") as save:
            self.assertTrue(json.load(save) != None)

if __name__ == '__main__':
    unittest.main()
        