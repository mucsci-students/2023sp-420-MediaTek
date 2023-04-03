'''
This file is meant to test the functions in Model.py.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import Model as Model
from MVC.model import wordlist as wordlist
import unittest
import json

# Instantiates a test case for the model.
class Model_test (unittest.TestCase):
    
    # Setup process for unit test.
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
            
        
    # Tests getGameState
    def test_getGameState(self):
        self.gameState = self.model.getGameState()
        self.assertEqual(self.gameState, self.p1.gameState)
    
    # Tests getLetters
    def test_getLetters(self):
        self.gameLetters = self.model.getLetter()
        lettersExpected = self.p1.gaUserLetters.upper()
        self.assertEqual(lettersExpected, self.gameLetters)
        
    # Tests getReqLetter
    def test_getReqLetter(self):
        self.reqLetter = self.model.getReqLetter()
        letterExpected = self.p1.gaReqLetter.upper()
        self.assertEqual(letterExpected, self.reqLetter)
    
    # Tests getGuessedWords
    def test_getGuessedWords(self):
        self.guessedWords = self.model.getGuessedWords()
        wordsExpected = self.p1.guessedList
        for w in wordsExpected:
            self.assertTrue(self.guessedWords.__contains__(w))
    
    # Tests getWordList
    def test_getWordList(self):
        self.list = self.model.getWordList()
        wordsExpected = self.wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters)
        for u in wordsExpected:
            if self.model.p1.guessedList.__contains__(u):
                wordsExpected.remove(u)
        self.assertEqual(len(wordsExpected), len(self.list))
    
    # Tests getPoints
    def test_getPoints(self):
        self.testPoints = self.model.getPoints()
        self.assertEqual(self.p1.points, self.testPoints)
    
    # Tests getPuzzleState
    def test_getPuzzleState(self):
        self.state = self.model.getGameState()
        self.assertEqual(0, self.state)
        
     # Tests getPuzzleTotal
    def test_getPuzzleTotal(self):
        self.total = self.model.getPuzzleTotal()
        totalExpected = self.p1.puzzleTotal
        self.assertEqual(totalExpected, self.total)
    
    # Tests getPuzzleRank
    def test_getPuzzleRank(self):
        self.rank = self.model.getPuzzleRank()
        self.assertEqual("Great", self.rank)
    
    # Tests updatePuzzleState0
    def test_updatePuzzleStateZero(self):
        self.model.updatePuzzleState0()
        self.assertEqual(0, self.model.getPuzzleState())
    
    # Tests updatePuzzleState1
    def test_updatePuzzleStateOne(self):
        self.model.updatePuzzleState1()
        self.assertEqual(1, self.model.getPuzzleState())
    
    # Tests calculateTotalPoints
    def test_calculateTotalPoints(self):
        self.model.calculateTotalPoints(wordBank=self.wl.generateWordList(self.p1.gaReqLetter, self.p1.gaUserLetters))
        assert self.p1.puzzleTotal == 897
        self.assertEqual(897, self.p1.puzzleTotal)
    
    # Tests checkPangram
    def test_checkPangram(self):
        
        # First test case: input "pangram" expecting it to be false.
        self.testOne = self.model.checkPangram(input="pangram")
        self.assertFalse(self.testOne)
        
        # Second test case: input "mediocre" expecting it to be true.
        self.testTwo = self.model.checkPangram(input="mediocre")
        self.assertTrue(self.testTwo)
        
        # Third test case: input "viability" expecting it to be true.
        self.testThree = self.model.checkPangram(input="viability")
        self.assertTrue(self.testThree)
        
        # Fourth test case: input "notanactualword" expecting it to be false.
        self.testFour = self.model.checkPangram(input="notanactualword")
        self.assertFalse(self.testFour)
    
    # Tests newPuzzleAuto
    def test_NewPuzzleAuto(self):
        self.testmodel = Model.model()
        self.testmodel.NewPuzzleAuto()
        
        # We're making sure a new puzzle is generated. All bases are covered in this test.
        self.assertTrue(self.testmodel.p1.gaUserLetters.isalpha() and len(self.testmodel.p1.gaUserLetters) == 7)
        self.assertTrue(self.testmodel.p1.gaReqLetter.isalpha() and len(self.testmodel.p1.gaReqLetter) == 1)      
        self.assertEqual(self.testmodel.p1.points, 0)
        self.assertGreater(len(self.testmodel.p1.getList), 0)
        self.assertGreater(self.testmodel.p1.puzzleTotal, 0)
        self.assertEqual(len(self.testmodel.p1.guessedList), 0)
    
    # Tests NewPuzzleBase
    def test_NewPuzzleBase(self):
        self.testmodel = Model.model()
        self.testPangram = "staring"
        self.testmodel.NewPuzzleBase(userInput=self.testPangram)
        
        # We're making sure a new puzzle is generated. All bases are covered in this test.
        self.assertTrue(self.testmodel.p1.gaUserLetters.isalpha() and len(self.testmodel.p1.gaUserLetters) == 7)
        self.assertTrue(self.testmodel.p1.gaReqLetter.isalpha() and len(self.testmodel.p1.gaReqLetter) == 1)      
        self.assertEqual(self.testmodel.p1.points, 0)
        self.assertGreater(len(self.testmodel.p1.getList), 0)
        self.assertGreater(self.testmodel.p1.puzzleTotal, 0)
        self.assertEqual(len(self.testmodel.p1.guessedList), 0)
    
    # Tests userGuess
    def test_userGuess(self):
        
        # First, generate a new puzzle with a base word.
        self.testmodel = Model.model()
        self.testPangram = "whiskey"
        self.testmodel.NewPuzzleBase(userInput=self.testPangram)
        
        # Force the required letter to be "k" for testing.
        self.testmodel.p1.gaReqLetter = "k"
        self.testmodel.p1.getList = self.wl.generateWordList("k", "whiskey")
        
        # First guess: input "whisk" expecting it to be true.
        guessOne = self.testmodel.userGuess(userInput="whisk")
        self.assertTrue(guessOne)
        self.assertTrue(self.testmodel.p1.guessedList.__contains__('whisk'))
        
        # Second guess: input "keys" expexcting it to be true.
        guessTwo = self.testmodel.userGuess(userInput="keys")
        self.assertTrue(guessTwo)
        self.assertTrue(self.testmodel.p1.guessedList.__contains__('keys'))
        
        # Third guess: input "shy" expecting it to be false.
        guessThree = self.testmodel.userGuess(userInput="shy")
        self.assertFalse(guessThree)
        self.assertFalse(self.testmodel.p1.guessedList.__contains__('shy'))
        
        # Fourth guess: input "high" expecting it to be false.
        guessFour = self.testmodel.userGuess(userInput="high")
        self.assertFalse(guessFour)
        self.assertFalse(self.testmodel.p1.guessedList.__contains__('high'))
        
        # Final guess: input "whiskey" expecting it to be true.
        guessFive = self.testmodel.userGuess(userInput="whiskey")
        self.assertTrue(guessFive)
        self.assertTrue(self.testmodel.p1.guessedList.__contains__('whiskey'))
    
    # Tests gameRank
    def test_gameRank(self):
        self.model.gameRank()
        self.assertEqual(self.model.p1.showRank, "Great")

# Runs unittest.main() when prompted.
if __name__ == '__main__':
    unittest.main()