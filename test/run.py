'''
This file runs all the tests in the test directory using unittest.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import IdentifyBaseWord_test
import savegame_test
import Model_test
import wordlist_test
import pangramdb_test
import wordstuff_test
import Commands_test
import unittest

'''
A test suite for unittest and code coverage.
All the functions from previous test files are
run in this suite. This suite can be run by
calling 'coverage run test/run.py' in a
terminal.
'''
def suite():
    
    suite = unittest.TestSuite()
    suite.addTest(Model_test.Model_test('test_resetGame'))
    suite.addTest(Model_test.Model_test('test_encryptWords'))
    suite.addTest(Model_test.Model_test('test_decryptWords'))
    suite.addTest(Model_test.Model_test('test_grabOurKey'))
    suite.addTest(Model_test.Model_test('test_AuthorField'))
    suite.addTest(Model_test.Model_test('test_getGameState'))
    suite.addTest(Model_test.Model_test('test_getLetters'))
    suite.addTest(Model_test.Model_test('test_getReqLetter'))
    suite.addTest(Model_test.Model_test('test_getGuessedWords'))
    suite.addTest(Model_test.Model_test('test_getWordList'))
    suite.addTest(Model_test.Model_test('test_getPoints'))
    suite.addTest(Model_test.Model_test('test_getPuzzleState'))
    suite.addTest(Model_test.Model_test('test_getPuzzleTotal'))
    suite.addTest(Model_test.Model_test('test_getPuzzleRank'))
    suite.addTest(Model_test.Model_test('test_updatePuzzleStateZero'))
    suite.addTest(Model_test.Model_test('test_updatePuzzleStateOne'))
    suite.addTest(Model_test.Model_test('test_calculateTotalPoints'))
    suite.addTest(Model_test.Model_test('test_checkPangram'))
    suite.addTest(Model_test.Model_test('test_lettersToList'))
    suite.addTest(Model_test.Model_test('test_NewPuzzleAuto'))
    suite.addTest(Model_test.Model_test('test_NewPuzzleBase'))
    suite.addTest(Model_test.Model_test('test_userGuess'))
    suite.addTest(Model_test.Model_test('test_gameRank'))
    suite.addTest(IdentifyBaseWord_test.IdentifyBaseWord_test('test_autoGame'))
    suite.addTest(IdentifyBaseWord_test.IdentifyBaseWord_test('test_baseGame'))
    suite.addTest(savegame_test.savegame_test('test_savegame'))
    suite.addTest(savegame_test.savegame_test('test_saveencryptedgame'))
    suite.addTest(wordlist_test.wordlist_test('test_generateWordList'))
    suite.addTest(wordlist_test.wordlist_test('test_checkLetters'))
    suite.addTest(pangramdb_test.pangramdb_test('test_randomBase'))
    suite.addTest(wordstuff_test.wordstuff_test('test_checkWord'))
    suite.addTest(Commands_test.Commands_test('test_savePuzzle'))
    suite.addTest(Commands_test.Commands_test('test_saveSecretPuzzle'))
    
    return suite

# Unittest will want this. It runs the suite when prompted.
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


