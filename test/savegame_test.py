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
from MVC.model.savegame import savegame as savegame
from MVC.model.savegame import saveencryptedgame as saveencryptedgame
from MVC.model import wordlist as wordlist
import unittest
import json
from cryptography.fernet import Fernet as fernet

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
        
        userLetters = "delicat"
        reqLetter = "a"
        guessedWords = ["delicate", "late", "date", "dial", "tale", "tail", "call", "called"]
        wordList = wordlist.generateWordList(reqLetter, userLetters)
        points = 27
        maxPoints = 678
        
        savegame(reqLetter, userLetters, points, maxPoints, guessedWords, wordList, "delicate")
        with open("delicate.json", "r") as save:
            self.assertTrue(json.load(save) != None)
        os.remove("delicate.json")
    
    # Tests the savegame's encryption method
    def test_saveencryptedgame(self):
        userLetters = "pangrms"
        reqLetter = "a"
        guessedWords = ["pangram", "pangrams", "grams", "gram"]
        wordList = wordlist.generateWordList(reqLetter, userLetters)
        excryptList = list()
        points = 20
        maxPoints = 100
        author = 'MediaTek'
        
        f = fernet("ipqzBB-cFSlZ4Fu9t7MF6szSBt-iNetGruZba41lCts=")
        for x in wordList:
            toBytes = x.encode()
            encBytes = f.encrypt(toBytes)
            encString = encBytes.decode()
            excryptList.append(encString)
        
        saveencryptedgame(reqLetter, userLetters, points, maxPoints, guessedWords, excryptList, author, "pangramenc")
        with open("pangramenc.json", "r") as save:
            self.assertTrue(json.load(save) != None)
        
        userLetters = "delicat"
        reqLetter = "a"
        guessedWords = ["delicate", "late", "date", "dial", "tale", "tail", "call", "called"]
        wordList = wordlist.generateWordList(reqLetter, userLetters)
        excryptList = list()
        points = 27
        maxPoints = 678
        author = 'MediaTek'
        
        f = fernet("ipqzBB-cFSlZ4Fu9t7MF6szSBt-iNetGruZba41lCts=")
        for x in wordList:
            toBytes = x.encode()
            encBytes = f.encrypt(toBytes)
            encString = encBytes.decode()
            excryptList.append(encString)
        
        saveencryptedgame(reqLetter, userLetters, points, maxPoints, guessedWords, excryptList, author, "delicant")
        with open("delicant.json", "r") as save:
            self.assertTrue(json.load(save) != None)
        os.remove("delicant.json")
        
        

if __name__ == '__main__':
    unittest.main()
        