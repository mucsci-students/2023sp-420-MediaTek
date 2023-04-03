import os

check_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(check_dir,".","combsbig.png")
abs_path = os.path.abspath(db_dir)
print(abs_path)