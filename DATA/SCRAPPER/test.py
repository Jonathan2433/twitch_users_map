import mysql.connector


bdd = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = bdd.cursor()

mycursor.execute("CREATE DATABASE twitch_user_map")