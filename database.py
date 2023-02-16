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

def checkWord(userInput):
    cursor.execute("SELECT word FROM dict WHERE EXISTS (SELECT word FROM dict WHERE :word = " + userInput + ")")

checkWord("abdomen")



con.commit() 
con.close()