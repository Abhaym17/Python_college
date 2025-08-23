import pymysql

conn = pymysql.connect(host="localhost",user="root",password="",database="test")
cursor = conn.cursor()
cursor.execute( "insert into data (`firstname`,`lastname`,`city`) VALUES ('abahy','f','df' ) ")
conn.commit()

conn.close()