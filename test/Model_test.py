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
    
    def test_gameLoadEnc(self):
        self.testModel = Model.model()
        self.testModel2 = Model.model()
        with open("test/whiskeyENC.json","r") as jsonFile:
            game = json.load(jsonFile)
        self.testModel.gameLoad(game)
        checkAuthor = game['Author']
        self.assertEqual(self.testModel.p1.author, checkAuthor)
        loaded = {
        "RequiredLetter": "a",
        "PuzzleLetters": "pangrms",
        "CurrentPoints": 20,
        "MaxPoints": 100,
        "GuessedWords": [
            "pangram",
            "pangrams",
            "grams",
            "gram"
        ],
    "SecretWordList": "gAAAAABkQb0C1UjZJXKNe4ynA14cGFPsPJxjxYg5aDvo2rQl7CyPYGrGdPkKEWUv-5n0a9mN1TMVtuWmk2jCUNHNvRTd7u2BufyRH8jyGkSoeDl0XW6ujIQpTRBvFffS6eYt61v-_DeGertPS_SzvFtUs9xypRPpLUlJw8Qy2KPRQYz4tJ1KcVTDw5hOTsNLu0whJ7d2uVjaYIrQgDBJL4FjqgizutyAWx67d5leRMddC3vZrkSEKHBseqxfn84FtYX-fz8wyQIDOZpVoKK2_V88i9Las2nAZRrjMUvLS94MmaaAasumR1eOKttre-bx2Zh9QXB2J1i2R99U4GBgU-tWiJBZs3xXIW-9ImFtBblt4pKmu5GblAqlNgtt1_Tu4DLQ5HnAJq8aWDJZyrjYtJrkXSRk_8uErVcjLg-jO4tCnNeLhWdUgiBatTE11Ab_7NGyfrnwFKEhLXpMHraDmrwhNfdQDNr__ftoU2nL_Z73QiX9tTeQ23WN796GeV6QTIm4vbMrJk76CCw8rmycAVOshGUPs3cfdrXqgXkQfaqrkXJRkURqU2-Zzl_b3k10R45jJW5nKgRRWgQ0QQHMWsNtU5jf9CIla6jgt8_h9oWMzdYLwL4vgz8zfOYg15SbUhsu5Vtn93UNaoXxMGu1i-LYZ7OwS69vmEhb5sFwh7SzS_ac1pdAZpAcUBpUokTQhsGpTHSQ9mWRZUgQ7c5n1qz129i2w60nc0gy7Xks-xC-mwK4iHYD91A2-OGpnJchn-k4xL7z2RkqyDjls5OyRW6Zlod_NJ_UAeUWdsHUzRgGf4Ah9iUfLmCiCyLBIOSnBZd2RUco_BXw_N8RjyST0gWnAq75iEgoYywJnW1Y8B-E5LdRYpUQe5H98V8NaCEWVud2BMLRmfYTL4o7gAFnL9EuJE9bNOr50y_YVYm5nuj-JySPUrZgsUhn99WJHsU3ksTVbiYNDrCuW0NFYERqckRrbjLgavIzX_hvBqqTsW8u85M8UE5yX9d4IfdfZbTkD-1x-2RgZjOH4K_KYvmb7AY4iof8nLCrCmOWMH6Lz6ovk-HHZp2kyRNLLbkySId5YV8DfL8eZ_aBJq3HDdgrOyZEz8miAzK1YxY18uzpNOczZhpl8oIPZu7p6FlrFyW2o_RSure835V6BftHkfkg4W8oRNXUcmkaSTfIBNdfnANWe0MPjnWydPUx8UJXjEtdgAH3Rhc_SD2Fj5a74WcQE3GftQi2e7AcStCkCnVohyuGfbARsgmYaA-F7w0SYiJGLsQzjALvOsFfrTnS8MeiSkbV7fpLF9iAOG50MAQvMpIKdinSN19rIuBU-VvO7Q748sNPv7L6n9haWlXJSMpDmB_BDyP9X4eyA6DPg39HNoyf_XUTZIm78c39kdDPcuZ7EmmF1oQuNmRwrzR6KBdAPvVJQRlfNcKYNku2_k5QbFAdlMwmpwYA4kVSSQnjTgzj4WF1Nvzx8yfG-dHLRzGAmTLz6mSqtX-yTcjHsUoJFt1d_konPI3V5H2hYvcpsTiSV0yV4v7X8O6DWs2dmUeksKVaYaXtUjsIKPrAzSoewpEy90yFFhe6BUrtUs-AmpHvgr9j4cDE83UcZboOGPy0-sDeDAuXeN1Uz6PRrm8aj4o7nCDYFDILhjyLwqwSsX7NHo13derCbBtpfzeZxDNUOTjR2I3g1lcmzJ207N3LA8c136jjPL6jzmuAUuxTX5F0U44YWX0s5t_7yzVKaGgiCpEJL_w857efUWeoD4ycHYE8OV9hjE3zGrA89UGOvWVNgpkugTu5O032HU0N72XMH1l9WsgULx8oqw1jXovh9dWl-thlZVaB41EaFgN_KtS4OJvKY3TsSqQho1bvNrU4OfOzgIvvfhXuBTHJMrChgWuBUQ4lERXbBu0NqB7XaoY_fy2Fww_GImyJ",
        "Author": "MediaTek"
        }

        # Call the gameLoad method with the sample 'loaded' dictionary
        self.testModel2.gameLoad(loaded)

        # Assert that the game object is updated with the correct values
        self.assertEqual(self.testModel2.p1.author, "MediaTek")
        self.assertEqual(self.testModel2.p1.author, loaded['Author'])
        self.assertEqual(self.testModel2.p1.encryptedList, '')
        self.assertEqual(self.testModel2.p1.gaReqLetter, loaded['RequiredLetter'])
        self.assertEqual(self.testModel2.p1.gaUserLetters, loaded['PuzzleLetters'])
        self.assertEqual(self.testModel2.p1.points, loaded['CurrentPoints'])
        self.assertEqual(self.testModel2.p1.puzzleTotal, loaded['MaxPoints'])
        self.assertEqual(self.testModel2.p1.guessedList, loaded['GuessedWords'])
        self.assertEqual(self.testModel2.p1.puzzleStarted, 1)
        
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
        self.testModel.p1.encryptedList = "gAAAAABkQcwJ58VC-xyeyDFLQbKh0S6aGpFk3xhmqY1XdXON88UJ7-pF_ASZcl_OmpGtdLQG5eCllKPWg3JU_h8ezdQvXarbGQ-u8mZqQwlhhCfNQr8eHbdhtYTlY8QEyKz_5bxrnEFg1_Va4L9TGx_Z6_69CFFKpGHptiDqIw3tjnyIAbMne0jMyvccN_jDTCE4kEPeMZtj8Z1vwOuy40MLU5PpbwyElQe9QC7tVudp_DUrjSduE9zmnfhGJ1zHD6SrP1EJ6m4W8XFTlp3fMdrxcAtg_YJobsQWjDwjMaqXtUC9Hoq2qJg8Zy2yKI8XqiPeX8odVFZPZKrmflG_pYt9FDqQlEJNrUc3d9kNdf6pJlTZ-xggm0kobRpagtoeadkMRwcRD213TbZDzV77gK-X8CTYuFiPNsbR74PJ1ymxq50F0fi7hH7zx_9ajrC7t1u-wQ2SqoqATyL4R8pN_RjNzr3dl6g1JpK0atsT3GkpGA_Ij53ZEQtFle119BMTGnhNqnEArUq5hk4CkwUNAy3beFeY_Y10zCJ8gIkUSIa3rvK_wzYcMXR8MWlgpm3lRfyYSIZXS4doLzWdzx6cCXHL_0vOH-sWauaigQtuxznx8h15oHGa7qapBL33gb-ppQHHKpr0fDMK-tnB5vnls5vyCbs33nw3ucEbtzF5G0PMpY79XxFD_v8lkLiDTTuG1Q3AtYvdcNwT3BB9HsCy6LIXIaGElNYtMhC5ljV8cByu6pXJ0VgruzAE1MTUFwgOk3kTsEv7p74TXKie6iZ0yG1LdsPvZEhxloFicjrSbADcXBQ4BQ7mAjcBu0p4H3DF0cLDH6KMpR7byySBIUob9x8MYbw3MxxTwOo7mFt6J5TrBlWaS2iU-8Qbo9VjaILQrAqUJ9SSzwbKTgyiEIzbgjgscOKeItwnJquWZo7KzYq-zas3j1Vn-xIBKfAZQA1VV9WjT7g9NJdqdLT4-ZBvfQYZMX399vFO9i1xhShWgtUiZR2SzBQUhcpOvenSeufWj_hq4Ibh2izXTkc4N88LUVtOllNhZqPSpL4pQRQC9QfPQNxqTJfmBT2XuVMFjOtvoSjWXIxxSXoe-2Lqu87U-6q3c42t7Wn-PCTsUgpfV8tO1V07oUJPr1mAq3TBE24EKIM--uzjEhZxxoNtDUtbs7pH901KW_CjHMVRsJs4PL8uxHypNixub63m8pzefYZ45TH9wDhU12c71TjerNAUfc0WKewGs-oYPHMo-UsuP8Mwn0Ee5UpMo345dE78vZDP5-bK46Z6hXgHLnQHZiXTLhNAHkJteMstsdaS36dV8e05FnRglrYb0HW8GcqsHgfpLAP1o-qd0TtxMyFds8gELuc0cDlR3MhlyUD1p-79mXUn53cwhdSAp6fwtd0-w14-yiQOZy9iLofp0H10cQOinf9YcygKBJ1B24S36pZ2YKmnePf1ftaFfuX3O9x6VfySuomfxUQNq0PzLcuFP9CRYMY_Ngq2DaPW_4CDKqOe4jEB-iSQlU2-XpngL9RWlrszBE1eIXNC7TKQHs71r1mIVLqJybg6MNfgSuBjZIL2vktnrlEILdEm9tHnNjv0XOd4tMIfxVI6OTG5HF9lcvMppP2P9tbFLZWBfTxYXgCY_hzvxYFw9kD2DbLM9nTWLqOEDAhgjI3rZtnzFbLQ26cqLmGE7BtfeGwrnITXrPXTzywZeG9LGd_38PRX5GZdtZTx-Jns-XTnvhkNa8qbc31bvDLaJKUKMgFTTRnDnCEQqBy7zO5aYdHTexB88KjYx6L1yIFwHxuciFdxDgVQAa-HGA8vydgZiyYKyvaOGRXjXLZnMntdcpYYIRq_3pcS7MSHO5_dT8fCQisCuAiifXv3aJ7ThQ789aOkmlCypjsBJEJITeEN1-_F2mw2Z6hB2rr-IdWP_6rUvaAl"
        
        self.testModel.encryptWords()
        f = fernet(self.testModel.p1.storeKey)
        
        x = ','.join(self.testModel.p1.getList)
        toBytes = x.encode()
        encryptBytes = f.encrypt(toBytes)
        encryptString = encryptBytes.decode()
        
        byteString = f.decrypt(self.testModel.p1.encryptedList.encode()).decode()
        secondString = f.decrypt(encryptString.encode()).decode()
        self.assertEqual(byteString, secondString)
        
    # Tests decryptWords
    def test_decryptWords(self):
        self.testList = ['word', 'words', 'only', 'head', 'variable', 'undermind', 'salty']
        self.testEncryptedString = str()
        self.testDecryptedList = list()
        self.testModel = Model.model()
        self.testModel.p1.getList = self.testList
        
        self.testModel.grabOurKey()
        f = fernet(self.testModel.p1.storeKey)
        
        x = ','.join(self.testModel.p1.getList)
        toBytes = x.encode()
        encryptBytes = f.encrypt(toBytes)
        encryptString = encryptBytes.decode()
        self.testModel.p1.encryptedList = encryptString
        self.testEncryptedString = encryptString
        
        self.testModel.decryptWords()
        self.testDecryptedList = f.decrypt(self.testEncryptedString.encode()).decode().split(',')
        self.assertEqual(self.testModel.p1.getList, self.testDecryptedList)

    # Tests authorField
    def test_AuthorField(self):
        self.testModel = Model.model()
        self.testModel.p1.author = "BLEH"
        self.testModel.updateAuthorField()
        self.assertEqual(self.testModel.p1.author, "MediaTek")

    def test_AuthorField2(self):
        self.testModel = Model.model()
        someVariable = self.testModel.getAuthorField()
        self.assertEqual(someVariable, self.testModel.p1.author)
    
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

        guessSix = self.testmodel.userGuess(userInput="kbcdefg")
        self.assertFalse(guessSix)

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
        honeyCombList = self.testModel.getHoneyCombList()
        self.testModel.lettersToList()
        self.assertEqual(str(self.testModel.p1.displayLetters),"['S', 'P', 'E', 'I', 'A', 'L']")
        self.assertEqual(str(honeyCombList),"['S', 'P', 'E', 'I', 'A', 'L']")

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