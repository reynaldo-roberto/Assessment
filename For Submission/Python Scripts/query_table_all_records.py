import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F3bru@ry!234",
    database="Assessment"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM BOM;")

result = cursor.fetchall()

for x in result:
  print(x)

print("\n")
cursor.execute("SELECT COUNT(*) FROM BOM")

result = cursor.fetchone()

row_count = result[0]

print("Number of Records in the table:", row_count, "\n")
print("Database Query Successful !!!")

#print("Database Query Successful !!!")

