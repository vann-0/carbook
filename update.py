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
sql = "UPDATE Car SET tel_number = 110 WHERE driver = '%c'" % ('1')

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
   print("execute successed")
  
except:
   # 如果发生错误则回滚
   db.rollback()
   print("execute failed")


db.close()