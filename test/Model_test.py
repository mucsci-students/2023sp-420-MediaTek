import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import Model as Model
from MVC.model import wordlist as wordlist
import unittest
import json

class Model_test:
    
    def __init__(self):
        self.model = Model.model
        with open("mediocre.json", "r") as jsonFile:
            game = json.load(jsonFile)
        self.model.gameLoad(self, game)
        
        self.reqLetter = game['RequiredLetter']
        self.userLetters = game['PuzzleLetters']
        self.points = game['CurrentPoints']
        self.maxPoints = game['MaxPoints']
        self.guessedWords = game['GuessedWords']
        self.wordList = game['WordList']
        
        self.wl = wordlist
            
        
    
    def getGameState_test(self):
        self.gameState = self.model.getGameState()
        assert self.gameState == self.player.gameState
    
    def getLetters_test(self):
        self.gameLetters = self.model.getLetter()
        lettersExpected = self.userLetters.upper()
        assert lettersExpected == self.gameLetter
    
    def getReqLetter_test(self):
        self.reqLetter = self.model.getReqLetter()
        letterExpected = self.reqLetter.upper()
        assert letterExpected == self.reqLetter
    
    def getGuessedWords_test(self):
        self.guessedWords = self.model.getGuessedWords()
        wordsExpected = self.guessedWords.upper()
        assert wordsExpected == self.guessedWords
    
    def getWordList_test(self):
        self.list = self.model.getWordList()
        wordsExpected = self.wl.generateWordList(self.reqLetter, self.userLetters)
        assert wordsExpected == self.list
    
    def getPoints_test(self):
        self.testPoints = self.model.getPoints()
        assert self.points == self.testPoints
    
    def getPuzzleState_test(self):
        self.state = self.model.getGameState()
        assert self.state == 1
    
    def getPuzzleTotal_test(self):
        self.total = self.model.getPuzzleTotal()
        totalExpected = self.maxPoints
        assert totalExpected == self.total
    
    def getPuzzleRank_test(self):
        self.rank = self.model.getPuzzleRank()
        assert self.rank == 'Great'
    
    def getHoneyCombList_test(self):
        self.letters = self.model.getHoneyCombList()
        # what should be asserted here?
    
    def updatePuzzleState0_test(self):
        self.model.updatePuzzleState0()
        assert self.model.getPuzzleState() == 0
    
    def updatePuzzleState1_test(self):
        self.model.updatePuzzleState1()
        assert self.model.getPuzzleState() == 1