import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F3bru@ry!234"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE Assessment")

print("Database Created Successful !!!")