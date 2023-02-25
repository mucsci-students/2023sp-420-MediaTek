import pytest
import modelrefactor
import controllerrefactor
import wordlist as WL
import IdentifyBaseWord as base

class gametest:
    
    self.testmodel = modelrefactor.model
    self.testcontroller = controllerrefactor.controller
    self.testLetters = "whiskey"
    self.testReq = "e"
    
    def modeltest(self):
        # Test get list
        self.testmodel.p1.gaUserLetters = self.testLetters
        self.testmodel.p1.gaReqLetter = self.testReq
        modellist = self.testmodel.wl.generateWordList(self.testmodel.p1.gaUserLetters, self.testmodel.p1.gaReqLetter)
        explist = WL.generateWordList(self.testLetters, self.testReq)
        assert not len(modellist) == 0
        assert not len(explist) == 0
        assert modellist == explist
        
        # Test auto game
        self.testLetters, self.testReq = self.testmodel.np.autoGame()
        assert not len(testLetters) == 0
        assert not len(testReq) == 0
        baseLetters, baseReq = base.autoGame()
        assert self.testLetters == baseLetters
        assert self.testReq == baseReq
        
        