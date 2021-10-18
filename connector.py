# importing necessary libraries
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    port='3306',
    database='hospital'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM patients")

patients = mycursor.fetchall()

for patient in patients:
    print(patient)



