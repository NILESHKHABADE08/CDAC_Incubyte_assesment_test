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
-----------------------------------------------------------------------------------------------------------------------------------------------------

MySQL Workbench patient table schema:


![image](https://user-images.githubusercontent.com/83622118/137672942-0641e04e-235f-49c1-86c8-34cfb3037829.png)
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


![image](https://user-images.githubusercontent.com/83622118/137672772-170dd5b7-1c13-4f41-8059-bab9a2da502a.png)

patients = mycursor.fetchall()

for patient in patients:
    print(patient)
