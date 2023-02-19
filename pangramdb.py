import sqlite3
import json
con = sqlite3.connect('pangrams.db')
cursor = con.cursor()

#SQLITE initializes table. do not need to run again since the table is already created !!!
#cursor.execute('''CREATE TABLE pangrams (pangram TEXT)''')


# Start with getting every word in the wordlist json.
'''
with open('pangram.json', "r") as wordbank:
    wordlist = json.load(wordbank)
for test in wordlist:
    cursor.execute("INSERT INTO pangrams VALUES (:word)", test)
'''

''' #Some code to print all the pangrams for testing purposes
cursor.execute("SELECT * FROM pangrams")
displayWords = cursor.fetchall()
for test2 in displayWords:
    print(test2)
'''
    
# function to choose a random pangram for use as the base word in a puzzle
def randomBase():
    cursor.execute("SELECT * FROM pangrams ORDER BY RANDOM() LIMIT 1;")
    randomPangram = cursor.fetchone()
    str = ''
    for item in randomPangram:
        str = str + item
    print(str)
    #return randomly chosen pangram
    return str


#SQLITE functions, neccessary
con.commit() 
#con.close()
