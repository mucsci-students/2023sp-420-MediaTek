import pytest
import MVC.model.modelrefactor as modelrefactor
import MVC.controller.controllerrefactor as controllerrefactor
import MVC.model.wordlist as WL
import MVC.model.IdentifyBaseWord as base
import json

class gametest:
    
    # Constructor
    def __init__(self):
        self.testmodel = modelrefactor.model
        self.testcontroller = controllerrefactor.controller
        self.testLetters = "whiskey"
        self.testReq = "e"
        
    
    # Test get list
    def testGetList(self):
        self.testmodel.p1.gaUserLetters = self.testLetters
        self.testmodel.p1.gaReqLetter = self.testReq
        modellist = self.testmodel.wl.generateWordList(self.testmodel.p1.gaUserLetters, self.testmodel.p1.gaReqLetter)
        explist = WL.generateWordList(self.testLetters, self.testReq)
        assert not len(modellist) == 0
        assert not len(explist) == 0
        assert modellist == explist
        
    # Test auto game
    def testAutoGame(self):
        self.testLetters, self.testReq = self.testmodel.np.autoGame()
        assert not len(testLetters) == 0
        assert not len(testReq) == 0
        baseLetters, baseReq = base.autoGame()
        assert self.testLetters == baseLetters
        assert self.testReq == baseReq
    
    # Test base game
    def testBaseGame(self):
        pangram = "mediocre"
        self.testLetters, self.ReqLetter = self.testmodel.np.baseGame()
        assert not len(self.testLetters) == 0
        assert not len(self.testReq) == 0
        for i in self.testLetters:
            assert not self.testLetters.find(1) == -1
    
    # Test save game
    def testSaveGame(self):
        self.testLetters = "whiskey"
        self.testReq = "e"
        gameName = "testName"
        self.testmodel.saveGame(gameName)
        assert not len(json.loads(gameName)) == 0
    
    # Test load game
    def testLoadGame(self):
        self.testLetters = "whiskey"
        self.testReq = "e"
        gameName = "testName"
        self.testmodel.gameLoad(gameName)
        assert not len(self.testmodel.p1.gaUseretters) == 0
        assert not len(self.testmodel.p1.gaReqetter) == 0
        assert self.testmodel.p1.gaUserLetters == self.testLetters
        assert self.testmodel.p1.gaReqLetter == self.testReq
