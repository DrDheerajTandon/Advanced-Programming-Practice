import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd='',database='srmdata')

mycursor = mydb.cursor()
mycursor.execute('Select * from student')

result = mycursor.fetchone()


print(result)
#for i in mycursor:
#	print(i)