import os
from MVC.database import connectDB as cdb


check_dir3 = os.path.dirname(os.path.abspath(__file__))
db_dir3 = os.path.join(check_dir3,".","highscores.db")
abs_path3 = os.path.abspath(db_dir3)


def highscore(self):
    con = cdb.highscoreConnect()
    c = con.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS highscores (
                    game_id TEXT,
                    player_name TEXT,
                    score INTEGER
                    )''')
    for row in c.execute('SELECT * FROM game_id;'):
        print(row)

    con.commit()
    con.close()
    

def saveHighScore(self, game_id, player_name, points):
    con = self._init_database(game_id)
    cursor = con.cursor()
    
    cursor.execute("INSERT INTO highscores (player_name, points) VALUES (?, ?)", (player_name, points))
    con.commit()
    con.close()


def loadHighScore(self, game_id, limit=10):
    con = self._init_database(game_id)
    cursor = con.cursor()
    
    cursor.execute("SELECT player_name, points FROM high_scores ORDER BY points DESC LIMIT ?", (limit))
    high_scores = cursor.fetchall()
    con.close()

    return [{"player_name": player_name, "points": points} for player_name, points in high_scores]


def generate_game_id(self):
    sorted_letters = sorted(self.userLetters)
    game_id = f"{self.reqLetter.upper()}{''.join(sorted_letters).upper()}"
    return game_id
