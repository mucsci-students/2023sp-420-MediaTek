'''
    File: wordlist.py
    Author: Devon F.
    Date: 2/2/2023
    Description: Takes a requird letter and set of unique letters
                 and returns a set of words from wordlist.json
                 containing word with only the unique letters and
                 the reequired letter.
    Version: 0.1
'''
# imports the json library
import json
# imports the sql library
import sqlite3
# Actual function itself
#words that user has guessed correctly
userWordList = []
rankWordList = []
def generateWordList (reqLetter, userLetter):
    fullwordlist = list()
    counter = 0
    
    # Start with getting every word in the wordlist json.
    con = sqlite3.connect('wordbank.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dict")
    # This next part took me 20 minutes :(
    draftwordlist = cursor.fetchall()
    fullwordlist = list()
    for i in draftwordlist:
        fullwordlist.append(i[0])
    
    # Split the userLetter string into a list.
    unique = list()
    for i in userLetter:
        unique.extend(i)
    
    # Get a list of every word that contains only the user's letters.
    userwordlist = list()
    for word in fullwordlist:
        # Use a separate function to check letters.
        if checkLetters(word, unique) == 0:
            # If there are no dissallowed characters, add it.
            userwordlist.append(word)
    
    # Get a list of every word that contains the required letter from the user word list.
    userunique = list()
    for word in userwordlist:
        # If the required letter exists in the word, add it.
        if word.count(reqLetter) >= 1:
            userunique.append(word)
            counter = counter + 1
    rankWordList = userunique
    #print("generateWordList:")
    #print(userunique)
    return userunique
    
# Checks a word for required letters.
def checkLetters(word, unique):
    value = 0 # Keeps a count of every character that's not allowed.
    for c in word:
        # If character not allowed, increment value by 1.
        if c not in unique:
            value = value + 1
    # return the value.
    return value
    

def storeWordList(theList):
    return theList

#generateWordList("e", "whisket")
#generateWordList("a", "abdomen")