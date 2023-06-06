import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    database='celulas_extra',
    user='root',
    password=''
)


cursor = con.cursor()