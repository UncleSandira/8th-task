import sqlite3

db = sqlite3.connect('Team.db')
cursor = db.cursor()

playername = input("Enter the player's name: ")
name = playername.title()

query = """
SELECT playerID, positionID, teamID FROM player
WHERE playerName = ?"""

cursor.execute(query, (name,))
result = cursor.fetchone()

if result is None:
    print(f"Player '{name}' not found in the database.")
else:
    playerID = result[0]
    positionID = result[1]
    teamID = result[2]

    print(f"Player information for {name}")
    print(f"Player ID: {playerID}")
    print(f"Position ID: {positionID}")
    print(f"Team ID: {teamID}")

db.close()
