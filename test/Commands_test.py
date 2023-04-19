import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import Model as Model
from MVC.model.Commands import savePuzzle as savePuzzle
from MVC.model.Commands import saveSecretPuzzle as saveSecretPuzzle
from cryptography.fernet import Fernet as fernet
from MVC.model import wordlist as wordlist
import json
import unittest

class Commands_test (unittest.TestCase):
    
    def setUp(self):
        self.model = Model.model()
    
    def test_savePuzzle(self):
        userLetters = "pangrms"
        reqLetter = "a"
        guessedWords = ["pangram", "pangrams", "grams", "gram"]
        wordList = wordlist.generateWordList(reqLetter, userLetters)
        points = 20
        maxPoints = 100
        
        # Unsure if this is the optimal way to test this but it's all I got with the knowlege I have.
        savePuzzle(reqLetter, userLetters, points, maxPoints, guessedWords, wordList, "pangram")
        with open("pangram.json", "r") as save:
            self.assertTrue(json.load(save) != None)
    
    def test_saveSecretPuzzle(self):
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
        
        saveSecretPuzzle(reqLetter, userLetters, points, maxPoints, guessedWords, excryptList, author, "pangramenc")
        with open("pangram.json", "r") as save:
            self.assertTrue(json.load(save) != None)

if __name__ == '__main__':
    unittest.main()