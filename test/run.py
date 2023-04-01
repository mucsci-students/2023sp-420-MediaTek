'''
This file runs all the tests in the test directory.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import IdentifyBaseWord_test
import savegame_test
import Model_test
import unittest

def suite():
    
    suite = unittest.TestSuite()
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
    suite.addTest(Model_test.Model_test('test_NewPuzzleAuto'))
    suite.addTest(Model_test.Model_test('test_NewPuzzleBase'))
    suite.addTest(IdentifyBaseWord_test.IdentifyBaseWord_test('test_autoGame'))
    suite.addTest(IdentifyBaseWord_test.IdentifyBaseWord_test('test_baseGame'))
    suite.addTest(savegame_test.savegame_test('test_savegame'))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


