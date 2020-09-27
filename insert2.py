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

# 查询操作
sql = "INSERT INTO Car(plate,brand,driver,tel_number) VALUES ('%s', '%s',  %s,  '%s')" % ('Mac4', 'Mohan', 20, 'M')

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