import pymysql 

conn = pymysql.connect(host="localhost",user="root",password="",database="test")
cursor = conn.cursor()
sql="SELECT* FROM  student"
cursor.execute(sql)
result=cursor.fetchall()
for row in result:
    print(row)
conn.close()