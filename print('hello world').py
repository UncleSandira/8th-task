import sqlite3

db = sqlite3.connect('Team.db')
cursor = db.cursor()
print('''Type "Team" if you want to check players in a certain team
or type "Stats" if you want to chekc a certain players stats''')

choose = input('Team/Stats: ').title()


if choose == "Stats":
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

elif choose == "Team":
    teamName = input('Enter name of the team: ')
    team = teamName.title()

    query2 = """
    SELECT playerName FROM player
    Where teamName = ?"""

    cursor.execute(query2, (teamName,))
    result2 = cursor.fetchall()

    if result2 is None:
        print(f'{team} not found in the database.')
    else:
        print(f"Team matching {team}")
        for people in result2:
            print(people[0])

db.close()
