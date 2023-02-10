import json

def savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints):
    inputFile = input("Please enter a name for the save file: ")
    try:
        with open(inputFile + ".json", "w") as save:
            json.dump([{'userLetters':userLetters}, {'requiredLetter':requiredLetter}, {'guessedWords':guessedWords}, {'wordBank':wordBank}, {'totalPoints':totalPoints}], save, indent=4)
    except FileNotFoundError():
        with open(inputFile + ".json", "x") as save:
            json.dump([{'userLetters':userLetters}, {'requiredLetter':requiredLetter}, {'guessedWords':guessedWords}, {'wordBank':wordBank}, {'totalPoints':totalPoints}], save, indent=4)
        