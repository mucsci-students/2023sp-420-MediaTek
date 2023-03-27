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
        self.model = Model.model()
        self.p1 = Model.player()
        with open("test/mediocre.json", "r") as jsonFile:
            game = json.load(jsonFile)
        self.model.gameLoad(game)
        
        self.p1.gaReqLetter = game['RequiredLetter']
        self.p1.gaUserLetters = game['PuzzleLetters']
        self.p1.points = game['CurrentPoints']
        self.p1.puzzleTotal = game['MaxPoints']
        self.p1.guessedList = game['GuessedWords']
        self.p1.getList = game['WordList']
        
        self.wl = wordlist
            
        
    
    def getGameState_test(self):
        self.gameState = self.model.getGameState()
        assert self.gameState == self.p1.gameState
    
    def getLetters_test(self):
        self.gameLetters = self.model.getLetter()
        lettersExpected = self.p1.gaUserLetters.upper()
        assert lettersExpected == self.gameLetters
        
    def getReqLetter_test(self):
        self.reqLetter = self.model.getReqLetter()
        letterExpected = self.p1.gaReqLetter.upper()
        assert letterExpected == self.reqLetter
    
    def getGuessedWords_test(self):
        self.guessedWords = self.model.getGuessedWords()
        wordsExpected = self.p1.guessedList
        for w in wordsExpected:
            assert self.guessedWords.__contains__(w)
    
    def getWordList_test(self):
        self.list = self.model.getWordList()
        wordsExpected = self.wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        for u in wordsExpected:
            if self.guessedWords.__contains__(u):
                wordsExpected.remove(u)
        assert len(wordsExpected) == len(self.list)
    
    def getPoints_test(self):
        self.testPoints = self.model.getPoints()
        assert self.p1.points == self.testPoints
    
    def getPuzzleState_test(self):
        self.state = self.model.getGameState()
        assert self.state == 0
    
    def getPuzzleTotal_test(self):
        self.total = self.model.getPuzzleTotal()
        totalExpected = self.p1.puzzleTotal
        assert totalExpected == self.total
    
    def getPuzzleRank_test(self):
        self.rank = self.model.getPuzzleRank()
        assert self.rank == "Great"
    
    def getHoneyCombList_test(self):
        self.letters = self.model.getHoneyCombList()
        # No idea what should be asserted here...
    
    def updatePuzzleState0_test(self):
        self.model.updatePuzzleState0()
        print(self.model.getPuzzleState())
        assert self.model.getPuzzleState() == 0
    
    def updatePuzzleState1_test(self):
        self.model.updatePuzzleState1()
        print(self.model.getPuzzleState())
        assert self.model.getPuzzleState() == 1