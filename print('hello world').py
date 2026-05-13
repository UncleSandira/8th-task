import sqlite3

db = sqlite3.connect('Team.db')
cursor = db.cursor()

player_name = input("Enter player name: ")
name = player_name.title()

 query = "SELECT positionID, positionName, teamID, teamName FROM player WHERE playerName = ?"
cursor.execute(query, (name,))
       

   