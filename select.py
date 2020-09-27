#!/usr/bin/python3
import pymysql

config={
    "host":"localhost",
    "user":"root",
    "password":"ZAQzaq1234-=",
    "db":"TESTDB"
}
db = pymysql.connect(**config)

cursor = db.cursor()
a=35

# 查询操作
sql = "SELECT * FROM Car \
       WHERE plate > %s" % (1)

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   # db.commit()
   print("execute successed")
   results=cursor.fetchall()
   for row in results:
     plate = row[0]
     brand = row[1]
     dirver = row[2]
     tel_number = row[3]
   print("plate=%s,brand=%s,dirver=%s,tel_number=%s" % \
      (plate, brand, dirver, tel_number ))
   # print(cursor.fetchall())

except:
   # 如果发生错误则回滚
   db.rollback()
   print("execute failed")


db.close()