'''
This file runs all the tests in the test directory.
It is not intended to be modified. Please submit a request if you
want to make changes to this file and the devlopers will decide if
the changes are valid.

- Devon
'''

import IdentifyBaseWord_test
import savegame_test

class run:
    
    # Initializes the class
    def __init__(self):
        self.test1 = IdentifyBaseWord_test.IdentifyBaseWord_test()
        self.test2 = savegame_test.savegame_test()
    
    # runs all the tests implemented so far
    def run(self):
        
        self.test1.autoGame_test()
        self.test1.baseGame_test()
        
        self.test2.savegame_test()
        
testRun = run()
testRun.run()