import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import model as mdl
from MVC.model import IdentifyBaseWord as base
from MVC.model import wordlist as wl
from MVC.model import savegame as save
from MVC.controller import controller as ctrl

# How many modules do we need? YES.
import unittest
import mock

class unittests:
    
    # Initialze the class
    def __init__(self):
        # Get Model and Controller classes
        self.model = mdl.model()
        self.controller = ctrl.controller()
        
        # Get model/controller properties
        self.player = mdl.player()
    
    # Helper function for sending input through the classes
    def input_function(self, default_response=None):
        
        def _input(prompt):
            return default_response if default_response else input(prompt)

        return _input
    
    # Tests for two invalid pangrams of different descriptions
    def testInvalidPangram(self):
        self.pangram = "pangram"
        with mock.patch('unittest.input', new=self.input_function(self.pangram)):
            self.userLetters, self.userReq = base.baseGame()
            assert self.userReq == "empty"
            assert self.userLetters == "empty"
        
        self.pangram = "psychiatrist"
        with mock.patch('unittest.input', new=self.input_function(self.pangram)):
            self.userLetters, self.userReq = base.baseGame()
            assert self.userReq == "empty"
            assert self.userLetters == "empty"
    
    # Tests with a valid pangram of seven letetrs in length
    def testPangramSevenLetters(self):
        self.pangram = "honesty"
        with mock.patch('unittest.input', new=self.input_function(self.pangram)):
            self.userLetters, self.userReq = base.baseGame()
            assert len(self.userReq) == 1
            assert len(self.userLetters) == 7
    
    # Tests the GUI version of BaseGame
    def testBaseGameGUI(self):
        self.pangram = "pangrams"
        self.gameLetters, self.gameReq = base.baseGameGUI(self.pangram)
        assert len(self.gameReq) == 1
        assert len(self.gameLetters) == 7
    
    # Tests auto game in IdentifyBaseWord
    def testAutoGame(self):
        self.gameLetters, self.gameReq = base.autoGame()
        assert len(self.gameReq) == 1
        assert len(self.gameLetters) == 7
        
    
    # Tests save and load functionality
    def testSaveAndLoad(self):
        self.gameLetters = "MEDIOCR"
        self.gameReq = "E"
        self.guesses = ['whiskey', 'hike', 'whisk']
        self.wordBank = wl.generateWordList(self.gameLetters, self.gameReq)
        self.points = 20
        self.maxPoints = self.model.calculateTotalPoints(self.wordBank)
        
        inputFile = "mediocre"
        save(self.gameReq, self.gameLetters, self.points, self.maxPoints, self.guesses, self.wordBank, inputFile)
        
        # Test CLI First
        self.model.gameLoadCLI(inputFile)
        self.loadLetters = self.model.p1.gaUserLetters
        self.loadReq = self.model.p1.gaReqLetter
        self.loadPoints = self.model.p1.points
        self.loadTotal = self.model.p1.puzzleTotal
        self.loadGuesses = self.model.p1.guessedList
        self.loadedWords = self.model.p1.getList
        
        assert len(self.loadLetters) == len(self.gameLetters)
        assert len(self.loadReq) == len(self.gameReq)
        assert self.loadPoints == self.points
        assert self.loadTotal == self.maxPoints
        assert len(self.loadGuesses) == len(self.guesses)
        assert len(self.loadedWords) == len(self.wordBank)
        
        # Test GUI Second
        inputFile = "mediocre.json"
        self.model.gameLoadGUI(inputFile)
        self.loadLetters = self.model.p1.gaUserLetters
        self.loadReq = self.model.p1.gaReqLetter
        self.loadPoints = self.model.p1.points
        self.loadTotal = self.model.p1.puzzleTotal
        self.loadGuesses = self.model.p1.guessedList
        self.loadedWords = self.model.p1.getList
        
        assert len(self.loadLetters) == len(self.gameLetters)
        assert len(self.loadReq) == len(self.gameReq)
        assert self.loadPoints == self.points
        assert self.loadTotal == self.maxPoints
        assert len(self.loadGuesses) == len(self.guesses)
        assert len(self.loadedWords) == len(self.wordBank)
            
ut = unittests()
ut.testAutoGame()
ut.testBaseGameGUI()
ut.testInvalidPangram()
ut.testPangramSevenLetters()
ut.testSaveAndLoad()
