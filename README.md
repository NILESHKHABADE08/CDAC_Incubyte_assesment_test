# CDAC_Incubyte_assesment_test

OVERVIEW :- 
This repository contains implementation of given assessment. The working of data pipeline is demonstarted using tools listed below. Also, a dummy database has been created to demonstarte a simple data flow in different formats from server to the local system, using country-based row filteration.

Concepts:

Data processing
Data visualization
ETL

Tools & Technologies: 
1)  Python
2)  MySQL Workbench
3)  MySQL connector 
---------------------------------------------------------------------------------------------------------------------------------------------

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
