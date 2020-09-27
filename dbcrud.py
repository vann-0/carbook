import pymysql
from md5lock import md5pwd

class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='ZAQzaq1234-='):
        # 建立连接 
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd)
        # 创建游标，操作设置为字典类型        
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标        
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行        
        self.conn.commit()
        # 关闭游标        
        self.cur.close()
        # 关闭数据库连接        
        self.conn.close()

if __name__ == '__main__':
    # unlockpwd=input()
    # lockpwd=md5pwd(unlockpwd)
    # with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
    #     sql = "INSERT INTO User(name,password,mail_address) VALUES ('%s', '%s',  '%s')" % ('Mohan',lockpwd , 'M')
    #     db.execute(sql)
    #     db.execute('select * from Car')
    #     # print(db)
        # for i in db:
            # print(i)
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        sql = "UPDATE Car SET tel_number = 110 WHERE driver = '%s'" % ('1')
        db.execute(sql)
        sql = "SELECT * FROM Car WHERE driver = %s" % ('1')
        db.execute(sql)
        results=[]
        for i in db:
            results.append(i)
        print(results)

        
