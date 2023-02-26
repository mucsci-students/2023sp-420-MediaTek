import json

def savegame(userLetters, requiredLetter, guessedWords, wordBank, totalPoints, maxPoints, inputFile):
    try:
        # If file exists, write to it.
        with open(inputFile + ".json", "w") as save:
            json.dump({"RequiredLetter": requiredLetter, "PuzzleLetters": userLetters, "CurrentPoints": totalPoints, "MaxPoints": maxPoints, "GuessedWords": guessedWords, "WordList": wordBank}, save, indent=4)
    except FileNotFoundError():
        # If not, create the file and them write.
        with open(inputFile + ".json", "x") as save:
            json.dump({"RequiredLetter": requiredLetter, "PuzzleLetters": userLetters, "CurrentPoints": totalPoints, "MaxPoints": maxPoints, "GuessedWords": guessedWords, "WordList": wordBank}, save, indent=4)
        