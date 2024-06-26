import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    mycursor = mydb.cursor()
    sql1 = "CREATE DATABASE libpro"
    mycursor.execute(sql1)
    mydb.commit()
    mydb.database = "libpro"
    sql2 = "CREATE TABLE member (mid INT(10) NOT NULL PRIMARY KEY, cid INT(10) NOT NULL, mname VARCHAR(30), madd VARCHAR(20), mtel INT(10),mregdate DATE,mnic VARCHAR(12),msection VARCHAR(20),mbdate DATE,mcfirm INT(1))"
    mycursor.execute(sql2)
    mydb.commit()

    mycursor = mydb.cursor()
    sql3 = "CREATE TABLE company (cid INT(10) NOT NULL PRIMARY KEY, cname CHAR(20), cadd VARCHAR(30), ctel INT(10))"
    mycursor.execute(sql3)
    mydb.commit

    print("\n\t\t\t Database and tables for 'Library project' created successfully.")
    print("\n\t\t\t Have a nice day !")
    x=1
    while True:
        if x==1:
            y=2
        else:
            y=3

except mysql.connector.Error as err:
    print(f"\n Error creating database or tables: {err}")
    x=1
    while True:
        if x==1:
            y=2
        else:
            y=3

finally:
    if mydb:
        mycursor.close()
        mydb.close()
