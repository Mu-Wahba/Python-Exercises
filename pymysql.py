import pymysql

connection = pymysql.connect(host='',db='',
                      user='',
                      passwd='')
cursor=connection.cursor()
try:
     cursor.execute("SELECT * FROM mytable")
     result = cursor.fetchall()
     print(result)
     connection.commit()
except Exception as e :
     print(e)
     connection.rollback()
finally:
     connection.close()
