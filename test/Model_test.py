import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import Model as Model
import unittest
import json

class Model_test:
    
    def __init__(self):
        self.model = Model.model
        self.player = Model.player
        with open("mediocre.json", "r") as jsonFile:
            game = json.load(jsonFile)
        self.model.gameLoad(self, game)
        
        self.reqLetter = game['RequiredLetter']
        self.userLetters = game['PuzzleLetters']
        self.points = game['CurrentPoints']
        self.maxPoints = game['MaxPoints']
        self.guessedWords = game['GuessedWords']
        self.wordList = game['WordList']
            
        
    
    def getGameState_test(self):
        self.gameState = self.model.getGameState()
        assert self.gameState == self.player.gameState
    
    def getLetters_test(self):
        self.gameLetters = self.model.getLetter()
        lettersExpected = self.userLetters.upper()
        assert lettersExpected == self.gameLetter
    
    
    
        