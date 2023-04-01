import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import Model as Model
from MVC.model import wordlist as wordlist
import unittest
import json

class Model_test (unittest.TestCase):
    
    def setUp(self):
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
            
        
    
    def test_getGameState(self):
        self.gameState = self.model.getGameState()
        self.assertEqual(self.gameState, self.p1.gameState)
    
    def test_getLetters(self):
        self.gameLetters = self.model.getLetter()
        lettersExpected = self.p1.gaUserLetters.upper()
        self.assertEqual(lettersExpected, self.gameLetters)
        
    def test_getReqLetter(self):
        self.reqLetter = self.model.getReqLetter()
        letterExpected = self.p1.gaReqLetter.upper()
        self.assertEqual(letterExpected, self.reqLetter)
    
    def test_getGuessedWords(self):
        self.guessedWords = self.model.getGuessedWords()
        wordsExpected = self.p1.guessedList
        for w in wordsExpected:
            self.assertTrue(self.guessedWords.__contains__(w))
    
    def test_getWordList(self):
        self.list = self.model.getWordList()
        wordsExpected = self.wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        for u in wordsExpected:
            if self.model.p1.guessedList.__contains__(u):
                wordsExpected.remove(u)
        self.assertEqual(len(wordsExpected), len(self.list))
    
    def test_getPoints(self):
        self.testPoints = self.model.getPoints()
        self.assertEqual(self.p1.points, self.testPoints)
    
    def test_getPuzzleState(self):
        self.state = self.model.getGameState()
        self.assertEqual(0, self.state)
    
    def test_getPuzzleTotal(self):
        self.total = self.model.getPuzzleTotal()
        totalExpected = self.p1.puzzleTotal
        self.assertEqual(totalExpected, self.total)
    
    def test_getPuzzleRank(self):
        self.rank = self.model.getPuzzleRank()
        self.assertEqual("Great", self.rank)
    
    def test_updatePuzzleStateZero(self):
        self.model.updatePuzzleState0()
        self.assertEqual(0, self.model.getPuzzleState())
    
    def test_updatePuzzleStateOne(self):
        self.model.updatePuzzleState1()
        self.assertEqual(1, self.model.getPuzzleState())
    
    def test_calculateTotalPoints(self):
        self.model.calculateTotalPoints(wordBank=self.wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters))
        assert self.p1.puzzleTotal == 897
        self.assertEqual(897, self.p1.puzzleTotal)
    
    def test_checkPangram(self):
        self.testOne = self.model.checkPangram(input="pangram")
        self.assertFalse(self.testOne)
        
        self.testTwo = self.model.checkPangram(input="mediocre")
        self.assertTrue(self.testTwo)
        
        self.testThree = self.model.checkPangram(input="viability")
        self.assertTrue(self.testThree)
        
        self.testFour = self.model.checkPangram(input="notanactualword")
        self.assertFalse(self.testFour)
    
    def test_NewPuzzleAuto(self):
        self.testmodel = Model.model()
        self.testmodel.NewPuzzleAuto()
        self.assertTrue(self.testmodel.p1.gaUserLetters.isalpha() and len(self.testmodel.p1.gaUserLetters) == 7)
        self.assertTrue(self.testmodel.p1.gaReqLetter.isalpha() and len(self.testmodel.p1.gaReqLetter) == 1)      
        self.assertEqual(self.model.p1.points, 0)
        self.assertGreater(len(self.testmodel.p1.getList), 0)
        self.assertGreater(self.testmodel.p1.puzzleTotal, 0)
        self.assertEqual(len(self.testmodel.p1.guessedList), 0)
    
    def test_NewPuzzleBase(self):
        self.testmodel = Model.model()
        self.testPangram = "jibberish"
        self.testmodel.NewPuzzleBase(userInput=self.testPangram)
        self.assertTrue(self.testmodel.p1.gaUserLetters.isalpha() and len(self.testmodel.p1.gaUserLetters) == 7)
        self.assertTrue(self.testmodel.p1.gaReqLetter.isalpha() and len(self.testmodel.p1.gaReqLetter) == 1)      
        self.assertEqual(self.model.p1.points, 0)
        self.assertGreater(len(self.testmodel.p1.getList), 0)
        self.assertGreater(self.testmodel.p1.puzzleTotal, 0)
        self.assertEqual(len(self.testmodel.p1.guessedList), 0)

if __name__ == '__main__':
    unittest.main()