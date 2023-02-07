import json

def savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints):
    with open('savegame.json', "w") as save:
        json.dump([{'userLetters':userLetters}, {'requiredLetter':requiredLetter}, {'guessedWords':guessedWords}, {'wordBank':wordBank}, {'totalPoints':totalPoints}], save, indent=4)

