#mysql-connector is installed using:
#python -m pip install mysql-connector

#mysql-connector is imported into python
import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user = "username",
  password = "password"
)
print(mydb)

#to check if any database is there in the server
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

