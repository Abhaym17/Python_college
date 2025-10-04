import pymysql 

con = pymysql.connect(host="localhost",user="root",password="",database="test")
cursor = con.cursor()
sql = "UPDATE `student` set `name`='darshan', `age`='21' where `id`='1' "
cursor.execute(sql)
con.commit()
