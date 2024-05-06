import mysql.connector

#create a connection with database
dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "URPASSWORDHERE"
)

#cretate a cursor
cursor = dataBase.cursor()

#create database
cursor.execute("CREATE DATABASE dcrm")

print('All done!')