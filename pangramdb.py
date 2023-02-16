import sqlite3
import json
con = sqlite3.connect('pangrams.db')
cursor = con.cursor()

#cursor.execute('''CREATE TABLE pangrams (pangram TEXT)''')


# Start with getting every word in the wordlist json.
'''
with open('pangram.json', "r") as wordbank:
    wordlist = json.load(wordbank)
for test in wordlist:
    cursor.execute("INSERT INTO pangrams VALUES (:word)", test)
'''


cursor.execute("SELECT * FROM pangrams")
displayWords = cursor.fetchall()
for test2 in displayWords:
    print(test2)



con.commit() 
con.close()