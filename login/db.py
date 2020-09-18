import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin',
    database='logindatabase'
    )

# print(db)

mycursor = db.cursor()

'''# mycursor.execute('CREATE DATABASE logindb')
#  mycursor.execute('CREATE TABLE person (id int PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255),email VARCHAR(255),password VARCHAR(255))')
mycursor.execute('DESCRIBE person')
for x in mycursor:
    print(x)
mycursor.execute('INSERT INTO person (name,email,password) VALUES (%s,%s,%s)', ('amit', 'amit@xyz.com', '12345'))
mycursor.execute('INSERT INTO person (name,email,password) VALUES (%s,%s,%s)', ('dhiraj', 'dhiraj@xyz.com', '12345'))
mycursor.execute('INSERT INTO person (name,email,password) VALUES (%s,%s,%s)', ('subho', 'subho@xyz.com', '12345'))
db.commit()

mycursor.execute('SELECT * FROM logindb')
for x in mycursor:
    print(x)'''
