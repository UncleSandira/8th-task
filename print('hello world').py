import sqlite3

db = sqlite3.connect('Team.db')
cursor = db.cursor()


def show_player():
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
def show_team():
    if choose == "Team":
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
            
def show_id():
    if choose == 'Id':
        playerID = int(input('Enter ID of player'))
        id = playerID.title()

        query3 = """
        Select * From player 
        Where playerID = ?"""

        cursor.excute(query3, (playerID))
        result3 = cursor.fethone()

        if result3 is None:
            print(f'Player with that ID is not in our database.')
        else:
            playerID = result3[0]
            playerName = result3[1]
            positionID = result3[2]
            positionName = result3[3]
            teamID = result3[4]
            teamName = result3[5]
            Goals = result3[6]

            print(f'Information for the player with the ID {id}')
            print(f'Player ID : {playerID}')
            print(f'Player Name : {playerName} ')
            print(f'Position ID : {positionID}')
            print(f'Position Name : {positionName}')
            print(f'Team ID : {teamID}')
            print(f'Team name : {teamName}')
            print(f'Goals scored : {Goals}')
def



print('''Type "Team" if you want to check players in a certain team
or type "Stats" if you want to chekc a certain players stats''')

choose = input('Team/Stats: ').title()

if choose == 'Stats':
    show_player()
elif choose == 'Team':
    show_team()

db.close()
