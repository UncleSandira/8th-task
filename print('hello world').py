import sqlite3

db = sqlite3.connect('Team.db')
cursor = db.cursor()

playerName = input("Enter player name: ")

cursor.execute("SELECT positionID, positionName, teamID, teamName FROM players WHERE playerName =?", (name,))

results = cursor.fetchone()

