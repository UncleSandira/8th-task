import sqlite3

db = sqlite3.connect('Team.db')
cursor=db.cursor()

playerName = input("Enter player name: ")
