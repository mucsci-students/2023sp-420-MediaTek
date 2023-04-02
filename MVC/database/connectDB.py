import sqlite3
import os


check_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(check_dir,".","pangrams.db")
abs_path = os.path.abspath(db_dir)
#print(abs_path)

check_dir2 = os.path.dirname(os.path.abspath(__file__))
db_dir2 = os.path.join(check_dir2,".","wordbank.db")
abs_path2 = os.path.abspath(db_dir2)
#print(abs_path2)


def pangramConnect():
   pangramConnection = None
   if pangramConnection is None:
      pangramConnection = sqlite3.connect(abs_path)
      return pangramConnection

def connect():
    conn = None
    if conn is None:
        conn = sqlite3.connect(abs_path2)
    return conn
