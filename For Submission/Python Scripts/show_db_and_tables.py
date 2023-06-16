import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F3bru@ry!234",
    database="Assessment"
)
cursor = db.cursor()

print("\n")
print("Current Database")
cursor.execute("SHOW DATABASES LIKE 'A%';")


for Database in cursor:
    print(Database)

print("\n")
print("Current Tables")

cursor.execute("SHOW TABLES;")

for Tables in cursor:
    print(Tables)
