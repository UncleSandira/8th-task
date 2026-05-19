import sqlite3

db = sqlite3.connect('Team.db')
cursor = db.cursor()


def show_player():
    if choose == "Stats":
        playername = input("Enter the player's name: ")
        name = playername.title()

        query = """
        SELECT playerID, positionID, teamID, Goals FROM player
        WHERE playerName = ?"""

        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result is None:
            print(f"Player '{name}' not found in the database.")
        else:
            playerID = result[0]
            positionID = result[1]
            teamID = result[2]
            Goals = result[3]

         
        print(f"Player information for {name}")
        print(f"Player ID: {playerID}")
        print(f"Position ID: {positionID}")
        print(f"Team ID: {teamID}")
        print(f'Goals scored : {Goals}')


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
            

def show_pos_name():
    if choose == 'Position Info':
        positionID = int(input('Enter position ID: '))
        id = positionID

        query3 = """
        Select positionName FROM position
        Where positionID = ?"""

        cursor.execute(query3, (id,))
        result3 = cursor.fetchone()

        if result3 is None:
            print('There is no such position in out database.')
        else:
            positionName = result3[0]
            
            print(f'Position information for position {id}')
            print(f'Position ID: {positionID}')
            print(f'Position Name: {positionName}')


def show_team_name():
    if choose == 'Team Name':
        teamId = int(input('Enter team ID:'))
        tID = teamId.upper()

        query4 = '''
        SELECT teamName FROM team
        WHERE teamID = ?'''

        cursor.execute(query4, (tID,))
        result4 = cursor.fetchone()
        if result4 is None:
            print('There is no such team with this id in ourt database.')
        else:
            teamName = result4[0]

            print(f'Team information for team {tID}')
            print(f'Team ID: {tID}')
            print(f'Team Name: {teamName}')


print('''Type "Team" if you want to check players in a certain team,
       type "Stats" if you want to chekc a certain players stats, 
      type "Position Info" if you want to check the position name of a certain position ID,
      type "Team Name" if you want to check the team name of a certain team ID''')

choose = input('Team/Stats/Position Info/Team Name: ').title()

if choose == 'Stats':
    show_player()
elif choose == 'Team':
    show_team()
elif choose == 'Position Info':
    show_pos_name()
elif choose == 'Team Name':
    show_team_name()

db.close()
