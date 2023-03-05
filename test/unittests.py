import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import modelrefactor as mdl
from MVC.model import IdentifyBaseWord as base
from MVC.model import wordlist as wl
from MVC.model import savegame as save
from MVC.controller import controllerrefactor as ctrl

# How many modules do we need? YES.
import unittest
import mock

class unittest:
    
    # Get Model and Controller classes
    self.model = mdl.model
    self.controller = ctrl.controller
    
    # Initialze the class
    def __init__(self):
        self.player = modelrefactor.player()
        self.model = modelrefactor.model()
        self.base = base
        self.savegame = save
        self.loadgame = load
    
    # Helper function for sending input through the classes
    def input_function(self, default_response=None):
        
        def _input(prompt):
            return default_response if default_response else input(prompt)

        return _input
    
    # Tests for two invalid pangrams of different descriptions
    def testInvalidPangram(self):
        self.pangram = "pangram"
        with mock.patch("base.input", new=input_function(self.pangram)):
            self.base.baseGame()
            assert self.model.getGameState() == 0
            assert len(self.model.getLetter()) == 0
        
        self.pangram = "psychiatrist"
        with mock.patch("base.input", new=input_function(self.pangram)):
            self.base.baseGame()
            assert self.model.getGameState() == 0
            assert len(self.model.getLetter()) == 0
    
    # Tests with a valid pangram of seven letetrs in length
    def testPangramSevenLetters(self):
        self.pangram = "honesty"
        with mock.patch("base.input", new=input_function(self.pangram)):
            self.base.baseGame()
            assert self.model.getGameState() == 1
            assert len(self.model.getLetter()) == 7
    
    # Tests save and load functionality
    def testSaveAndLoad(self):
        self.gameLetters = "mediocr"
        self.gameReq = "e"
        self.guesses = ['whiskey', 'hike', 'whisk']
        self.wordBank = wl.generateWordList(self.gameLetters, self.gameReq)
        self.points = 20
        self.maxPoints = self.model.calculateTotalPoints(self.wordBank)
        
        inputFile = "mediocre"
        save.savegame(self.gameReq, self.gameLetters, self.points, self.maxPoints, self.guesses, self.wordBank, inputFile)
        
        self.model.gameLoad(inputFile)
        self.loadLetters = self.model.p1.gaUserLetters
        self.loadReq = self.model.p1.gaReqLetter
        self.loadPoints = self.model.p1.points
        self.loadTotal = self.model.p1.puzzleTotal
        self.loadGuesses = self.model.p1.guessedList
        self.loadedWords = self.model.p1.getList
        
        assert self.loadLetters == self.gameLetters
        assert self.loadReq == self.gameReq
        assert self.loadPoints == self.points
        assert self.loadTotal == self.maxPoints
        assert self.loadGuesses == self.guesses
        assert self.loadedWords == self.wordBank
            

print(ctrl.controller.controllerGetLetters())