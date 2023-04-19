'''
This file is meant to test the functions in Model.py.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''
import random
import os
import sys
getPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'mvc'))
sys.path.append(getPath)
from MVC.model import Model as Model
from MVC.model import wordlist as wordlist
import unittest
import json
from cryptography.fernet import Fernet as fernet

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
    
    #Tests resetGame
    def test_resetGame(self):
        self.model.resetGame()
        
        # Test to see if everything actually got reset.
        self.assertEqual(len(self.model.p1.gaReqLetter), 0)
        self.assertEqual(len(self.model.p1.gaUserLetters), 0)
        self.assertEqual(self.model.p1.points, 0)
        self.assertEqual(self.model.p1.puzzleTotal, 0)
        self.assertEqual(len(self.model.p1.getList), 0)
        self.assertEqual(self.model.p1.gameState, 0)
        self.assertEqual(self.model.p1.puzzleStarted, 0)
        self.assertEqual(len(self.model.p1.displayLetters), 0)
        self.assertEqual(len(self.model.p1.encryptedList), 0)
        self.assertEqual(self.model.p1.storeKey, None)
        self.assertEqual(self.model.p1.author, "MediaTek")
        self.assertEqual(self.model.p1.game_id, None)
    
    # Tests encryptWords
    def test_encryptWords(self):
        self.testList = ['word', 'words', 'only', 'head', 'variable', 'undermind', 'salty']
        self.testEncryptedList = list()
        self.testModel = Model.model()
        self.testModel.p1.getList = self.testList
        
        self.testModel.encryptWords()
        f = fernet(self.testModel.p1.storeKey)
        for x in self.testList:
            toBytes = x.encode()
            encryptBytes = f.encrypt(toBytes)
            encryptString = encryptBytes.decode()
            self.testEncryptedList.append(encryptString)
        
        i = 0
        while (i < len(self.testEncryptedList)):
            x = f.decrypt(self.testEncryptedList[i]).decode()
            y = f.decrypt(self.testModel.p1.encryptedList[i]).decode()
            self.assertEqual(x, y)
            i = i + 1
    
    # Tests decryptWords
    def test_decryptWords(self):
        self.testList = ['word', 'words', 'only', 'head', 'variable', 'undermind', 'salty']
        self.testEncryptedList = list()
        self.testDecryptedList = list()
        self.testModel = Model.model()
        self.testModel.p1.getList = self.testList
        
        self.testModel.grabOurKey()
        f = fernet(self.testModel.p1.storeKey)
        for x in self.testList:
            toBytes = x.encode()
            encryptBytes = f.encrypt(toBytes)
            encryptString = encryptBytes.decode()
            self.testModel.p1.encryptedList.append(encryptString)
        
        f = fernet(self.testModel.p1.storeKey)
        for x in self.testList:
            toBytes = x.encode()
            encryptBytes = f.encrypt(toBytes)
            encryptString = encryptBytes.decode()
            self.testEncryptedList.append(encryptString)
        
        self.testModel.decryptWords()
        for x in self.testEncryptedList:
            decryptByteString = f.decrypt(x)
            decryptWord = decryptByteString.decode()
            self.testDecryptedList.append(decryptWord)
        
        i = 0
        while (i < len(self.testDecryptedList)):
            x = self.testModel.p1.getList[i]
            y = self.testDecryptedList[i]
            self.assertEqual(x, y)
            i = i + 1

    # Tests authorField
    def test_AuthorField(self):
        self.testModel = Model.model()
        self.testModel.p1.author = "BLEH"
        self.testModel.updateAuthorField()
        self.assertEqual(self.testModel.p1.author, "MediaTek")
    
    # Tests grabOurKey
    def test_grabOurKey(self):
        self.model.grabOurKey()
        decodeString = self.model.p1.storeKey.decode()
        self.assertEqual(decodeString, "ipqzBB-cFSlZ4Fu9t7MF6szSBt-iNetGruZba41lCts=")
        
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
        
        self.testPangram = "notapangram"
    
    def test_lettersToList(self):
        self.testModel = Model.model()
        
        # First test: "pangrams"
        self.testModel.p1.gaUserLetters = "pangrms"
        self.testModel.p1.gaReqLetter = "g"
        self.testModel.lettersToList()
        self.assertEqual(str(self.testModel.p1.displayLetters), "['P', 'A', 'N', 'R', 'M', 'S']")
        
        # Second Test: "whiskey"
        self.testModel.p1.gaUserLetters = "whiskey"
        self.testModel.p1.gaReqLetter = "e"
        self.testModel.lettersToList()
        self.assertEqual(str(self.testModel.p1.displayLetters), "['W', 'H', 'I', 'S', 'K', 'Y']")
    
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
        self.testModel = Model.model()
        self.testModel.p1.puzzleTotal = 678
        
        self.testModel.p1.points = 0
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Beginner")
        
        self.testModel.p1.points = (1*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Beginner")
        
        self.testModel.p1.points = (3*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Good")
        
        self.testModel.p1.points = (6*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Great")
        
        self.testModel.p1.points = (10*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Novice")
        
        self.testModel.p1.points = (15*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Amazing")
        
        self.testModel.p1.points = (25*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Advanced")
        
        self.testModel.p1.points = (50*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Expert")
        
        self.testModel.p1.points = (75*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Master")
        
        self.testModel.p1.points = (100*self.testModel.p1.puzzleTotal)/100
        self.testModel.gameRank()
        self.assertEqual(self.testModel.p1.showRank, "Puzzle Finished! Good Job!")
        
    def test_displayLetters(self):
        self.testModel = Model.model()
        self.testModel.p1.gaUserLetters = "special"
        self.testModel.p1.gaReqLetter = "c"
        self.testModel.lettersToList()
        self.assertEqual(str(self.testModel.p1.displayLetters),"['S', 'P', 'E', 'I', 'A', 'L']")

    def test_shuffleAuto(self):
        self.testModel = Model.model()
        self.testModel.p1.gaUserLetters = "mediocr"
        self.testModel.p1.gaReqLetter = "i"
        replaceString = self.testModel.p1.gaUserLetters.replace("[","").replace("]","")
        toList = list(replaceString)
        random.shuffle(toList)
        shuffledLetters = ''.join(toList)
        self.testModel.p1.gaUserLetters = shuffledLetters
        self.testModel.lettersToList()

        self.wtf = self.testModel.shuffleAuto()
        
        self.assertIn('M',self.testModel.p1.displayLetters)
        self.assertIn('E',self.testModel.p1.displayLetters)
        self.assertIn('D',self.testModel.p1.displayLetters)
        self.assertIn('O',self.testModel.p1.displayLetters)
        self.assertIn('C',self.testModel.p1.displayLetters)
        self.assertIn('R',self.testModel.p1.displayLetters)
        self.assertEqual(set(shuffledLetters),set(self.testModel.p1.gaUserLetters))
        self.assertEqual(set(self.wtf), set(self.testModel.p1.gaUserLetters))
# Runs unittest.main() when prompted.
if __name__ == '__main__':
    unittest.main()