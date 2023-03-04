'''
import unittest
from unittest import mock
import savegame
import loadgame
import modelrefactor
import IdentifyBaseWord as base


class unittest:
    
    def __init__(self):
        self.player = modelrefactor.player()
        self.model = modelrefactor.model()
        self.base = base
        
    def input_function(self, default_response=None):
        
        def _input(prompt):
            return default_response if default_response else input(prompt)

        return _input
    
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
    
    def testPangramSevenLetters(self):
        self.pangram = "honesty"
        with mock.patch("base.input", new=input_function(self.pangram)):
            self.base.baseGame()
            assert self.model.getGameState() == 1
            assert len(self.model.getLetter()) == 7
            
    def 
'''