import mysql.connector
import time

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="F3bru@ry!234",
    database="Assessment"
)
cursor = db.cursor()
print("\n")
print("Hello, welcome and my name is Rey and my job is to backup tables for databases.\n")

name = input("What is your name? ")

print("\n")
print("Hello " + name + ", thank you so much for coming in today.\n")

time.sleep(2)

print("Below is our list of Databases and Tables")

print("Current Database")
cursor.execute("SHOW DATABASES LIKE 'A%';")

time.sleep(2)
for Database in cursor:
    print(Database)

print("\n")
print("Current Tables")

cursor.execute("SHOW TABLES")

for Tables in cursor:
    print(Tables)

print("\n")
tbl = input("Which table would you like to backup? ")

time.sleep(1)
print("\n" + "Thank you " + name + ", table " + tbl + " will be backed up in a moment.")
time.sleep(2)
print("\n")

tbl_bkp = input("Please provide a name for your table backup, ensure there are no spaces. \n")
print("\n")


print(tbl + " will be backed up and named as " + tbl_bkp)

time.sleep(2)

# cursor.execute("DROP TABLE IF EXISTS " + tbl)
cursor.execute("CREATE TABLE " + tbl_bkp + " SELECT * FROM " + tbl)

print("\n")
print("Updated list of Tables and backup (" + tbl_bkp + ") has been created.")

cursor.execute("SHOW TABLES")

for Tables in cursor:
    print(Tables)
print("\n")

print("Thank you " + name + ", and have a nice day!!!")
time.sleep(2)
