import sqlite3
import json
import os
from MVC.model import connectDB as cdb
#con = sqlite3.connect('pangrams.db')
#cursor = con.cursor()

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
check_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(check_dir,".","pangrams.db")
abs_path = os.path.abspath(db_dir)
# function to choose a random pangram for use as the base word in a puzzle
def randomBase():
    con = cdb.pangramConnect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pangrams ORDER BY RANDOM() LIMIT 1;")
    randomPangram = cursor.fetchone()
    str = ''
    for item in randomPangram:
        str = str + item
    #print(str)
    #return randomly chosen pangram
    con.commit()
    con.close()
    return str



#test = randomBase()
#while len(test) != 15:
    #test = randomBase()
#randomBase()