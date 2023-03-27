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

class run:
    
    # Initializes the class
    def __init__(self):
        self.test1 = IdentifyBaseWord_test.IdentifyBaseWord_test()
        self.test2 = savegame_test.savegame_test()
        self.modeltest = Model_test.Model_test()
    
    # runs all the tests implemented so far
    def run(self):
        
        self.test1.autoGame_test()
        self.test1.baseGame_test()
        
        self.test2.savegame_test()
        
        '''
        self.modeltest.getGameState_test()
        self.modeltest.getGuessedWords_test()
        self.modeltest.getHoneyCombList_test()
        self.modeltest.getLetters_test()
        self.modeltest.getPoints_test()
        self.modeltest.getPuzzleRank_test()
        self.modeltest.getPuzzleState_test()
        self.modeltest.getPuzzleTotal_test()
        self.modeltest.getReqLetter_test()
        self.modeltest.getWordList_test()
        '''
        
        
testRun = run()
testRun.run()