import sqlite3
import json
con = sqlite3.connect('wordbank.db')
cursor = con.cursor()

#cursor.execute('''CREATE TABLE dict (word TEXT)''')


# Start with getting every word in the wordlist json.
'''
with open('wordbank.json', "r") as wordbank:
    wordlist = json.load(wordbank)
for test in wordlist:
    cursor.execute("INSERT INTO dict VALUES (:word)", test)
'''
'''
cursor.execute("SELECT * FROM dict")
displayWords = cursor.fetchall()
for test2 in displayWords:
    print(test2)
'''

'''
We want checkWord to return true
Because inside of IdentifyBaseWord we can set a variable equal to the function passing the userInput
If this is true we can manipulate the userInput and get the unique letters, and the required letter
'''

'''
For the random function, if it's possible to return the word that's randomly chosen from the database that would be great.s
'''

#for base game
def checkWord(userInput):
    con = sqlite3.connect('wordbank.db')
    cursor = con.cursor()
    #sql query to find the word
    cursor.execute("SELECT * FROM dict WHERE word=:word", {'word': userInput})
    #Because fetchone, fetches the next row returns this to a variable.
    test = cursor.fetchone()
    #check if it's none, if so return false.
    if (test == None):
        con.commit()
        con.close()
        return False
    #turn the tuple into a string
    else:
        str = ''
        for item in test:
            str = str + item
    #check if the string and user input matches.
    if str == userInput:
        con.commit()
        con.close()
        return True
    else:
        con.commit()
        con.close()
        return False





con.commit() 
