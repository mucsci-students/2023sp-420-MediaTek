import os
from MVC.database import connectDB as cdb


check_dir3 = os.path.dirname(os.path.abspath(__file__))
db_dir3 = os.path.join(check_dir3,".","highscores.db")
abs_path3 = os.path.abspath(db_dir3)

'''
creates the highscores table in the highscore database
'''
def create_highscores_table():
    con = cdb.highscoreConnect()
    c = con.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS highscores (
                    game_id TEXT,
                    player_name TEXT,
                    points INTEGER
                    )''')

    con.commit()
    con.close()

'''
saves highscore for a specific game_id along with player name and points scored to the aforementioned database.
game_id (str): The unique identifier for the game.
player_name (str): The player's name.
points (int): The player's points.
'''
def saveHighScore(game_id, player_name, points):
    con = cdb.highscoreConnect()
    cursor = con.cursor()

    cursor.execute("INSERT INTO highscores (game_id, player_name, points) VALUES (?, ?, ?)", (game_id, player_name, points))
    con.commit()
    con.close()

'''
Loads the top ten local highscores for a specific game_id
game_id (str): The unique identifier for the game.
limit (int, optional): The number of high scores to retrieve. Defaults to 10.
returns:
list[dict]: A list of dictionaries with the player's name and points.
'''
def loadHighScore(game_id):
    con = cdb.highscoreConnect()
    cursor = con.cursor()

    #Retrieve the top 10 high scores for the given game_id
    cursor.execute("SELECT game_id, player_name, points FROM highscores WHERE game_id = ? ORDER BY points DESC LIMIT 10", (game_id,))
    rows = cursor.fetchall()

    con.close()
    return rows

'''
Call create_highscores_table to ensure the table exists before any operations
'''
create_highscores_table()
