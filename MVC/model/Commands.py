from MVC.model import wordlist as wl
from MVC.model import savegame as savegame


def savePuzzle(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, maxPoints, inputFile):
    savegame.savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, maxPoints, inputFile)

#for saving an encrypted game, same as above but just passing in the encrypted word bank.
def saveSecretPuzzle(userLetters,requiredLetter,guessedWords,encryptedBank,totalPoints,maxPoints, author, inputFile):
    savegame.saveencryptedgame(userLetters, requiredLetter, guessedWords, encryptedBank, totalPoints, maxPoints, author, inputFile)