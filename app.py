import json
import os
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash, jsonify
import logging
from datetime import datetime

from timecheck import is_valid_date
from dbcrud import DB
import pymysql
from md5lock import md5pwd

LOGGER = logging.getLogger(__name__)

app = Flask(__name__)        
@app.route('/data/cars', methods=['GET'])
def get_cars():
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        plate = request.values.get("plate")
        sql = "SELECT * FROM Car WHERE plate = '%s'" % (plate)
        db.execute(sql)
        results=[]
        for i in db:
            results.append(i)
        if results==[]:
            results=["not found"]
        return json.dumps(results).encode()

@app.route('/data/car', methods=['GET','PUT'])
def insert_car():
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        plate = request.values.get("plate")
        brand = request.values.get("brand")
        driver = request.values.get("driver")
        tel_number = request.values.get("tel_number")  
        results=[]
        if plate==None:
            results=["Please input plate number!"]
        else:
            sql = "SELECT * FROM Car WHERE plate = '%s'" % (plate)
            db.execute(sql)        
            for i in db:
                results.append(i)     
            if results==[]:
                sql = "INSERT INTO Car(plate,brand,driver,tel_number) VALUES ('%s', '%s',  '%s',  '%s')" % (plate,brand,driver,tel_number)
                db.execute(sql)
                sql = "SELECT * FROM Car order by id_car desc limit 1;"
                db.execute(sql)
                results=[]
                for i in db:
                    results.append(i)
            else:
                results=["Plate number already existed!"] 
        return json.dumps(results).encode()

@app.route('/data/car/<id>', methods=['PATCH','GET'])
def update_car(id):
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:      
        plate = request.values.get("plate")
        brand = request.values.get("brand")
        driver = request.values.get("driver")
        tel_number = request.values.get("tel_number")
        results=[] 
        if plate==None:
            results=["Please input plate number!"] 
        else:
            sql = "UPDATE Car SET plate = '%s', brand = '%s', driver = '%s', tel_number = '%s' WHERE id_car = '%s'" % (plate,brand,driver,tel_number,id)
            db.execute(sql)
            sql = "SELECT * FROM Car WHERE id_car = '%s'" % (id)
            db.execute(sql)
            for i in db:
                results.append(i)
        return json.dumps(results).encode()

@app.route('/data/cars/<id>', methods=['DELETE','GET'])
def delete_car(id):
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        sql = "DELETE from Car WHERE id_car = '%s'" % (id)
        db.execute(sql)
        sql = "SELECT * FROM Car WHERE id_car = '%s'" % (id)
        db.execute(sql)
        results=[]
        for i in db:
            results.append(i)
        if results==[]:
            answer=["ok"]
        else:
            answer=["failed"]
        sql = "alter table Car drop column id_car;"
        db.execute(sql)
        sql = "alter table Car add id_car int not null primary key auto_increment first;"
        db.execute(sql)
        return json.dumps(answer).encode()

@app.route('/data/users', methods=['GET'])
def get_users():
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        name = request.values.get("name")
        sql = "SELECT * FROM User WHERE name = '%s'" % (name)
        db.execute(sql)
        results=[]
        for i in db:
            results.append(i)
        if results==[]:
            results=["not found"]
        return json.dumps(results).encode()

@app.route('/data/user', methods=['GET','PUT'])
def insert_user():
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        name = request.values.get("name")
        password = request.values.get("password")
        mail_address = request.values.get("mail_address")  
        results=[]
        if name==None or password ==None:
            results=["Please input user name and password!"]
        else:
            sql = "SELECT * FROM User WHERE name = '%s'" % (name)
            db.execute(sql)        
            for i in db:
                results.append(i)     
            if results==[]:
                sql = "INSERT INTO User(name,password,mail_address) VALUES ('%s', '%s',  '%s')" % (name,md5pwd(password),mail_address)
                db.execute(sql)
                sql = "SELECT * FROM User order by id_user desc limit 1;"
                db.execute(sql)
                results=[]
                for i in db:
                    results.append(i)
            else:
                results=["User name already existed!"] 
        return json.dumps(results).encode()

@app.route('/data/user/<id>', methods=['PATCH','GET'])
def update_user(id):
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:      
        name = request.values.get("name")
        password = request.values.get("password")
        mail_address = request.values.get("mail_address") 
        results=[] 
        if name==None or password==None:
            results=["Please input user name and password!"]
        else:
            sql = "UPDATE User SET name = '%s', password = '%s', mail_address = '%s' WHERE id_user = '%s'" % (name,md5pwd(password),mail_address,id)
            db.execute(sql)
            sql = "SELECT * FROM User WHERE id_user = '%s'" % (id)
            db.execute(sql)
            for i in db:
                results.append(i)
        
        return json.dumps(results).encode()

@app.route('/data/users/<id>', methods=['DELETE','GET'])
def delete_user(id):
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        sql = "DELETE from User WHERE id_user = '%s'" % (id)
        db.execute(sql)
        sql = "SELECT * FROM User WHERE id_user = '%s'" % (id)
        db.execute(sql)
        results=[]
        for i in db:
            results.append(i)
        if results==[]:
            answer=["ok"]
        else:
            answer=["failed"]
        sql = "alter table User drop column id_user;"
        db.execute(sql)
        sql = "alter table User add id_user int not null primary key auto_increment first;"
        db.execute(sql)
        return json.dumps(answer).encode()

@app.route('/data/carusages', methods=['GET'])
def get_carusages():
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        plate = request.values.get("plate")
        request_start_time = request.values.get("request_start_time")
        request_end_time = request.values.get("request_end_time")
        sql = "SELECT * FROM CarUsage WHERE plate = '%s' and end_time >= '%s' and start_time <= '%s'" % (plate,request_start_time,request_end_time)
        db.execute(sql)
        results=[]
        for i in db:
            results.append(i)
        if results==[]:
            results=["not found"]
        return json.dumps(results, indent=4, sort_keys=True, default=str).encode()

@app.route('/data/carusage', methods=['GET','PUT'])
def insert_carusage():
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        plate = request.values.get("plate")
        user = request.values.get("user")
        start_time = request.values.get("start_time")  
        end_time = request.values.get("end_time")
        results=[]
        if plate==None or start_time ==None or end_time ==None:
            results=["Please input booking information!"]
        elif is_valid_date(start_time)==False or is_valid_date(end_time)==False:
            results=["Please input right time!"]
        else:
            if start_time>=end_time:
                results=["Start time must earlier than end time!"] 
            else:                
                sql = "SELECT * FROM CarUsage WHERE plate = '%s' and ((start_time <= '%s' and '%s'<= end_time) or (start_time <= '%s' and '%s'<= end_time))" % (plate,start_time,start_time,end_time,end_time)
                db.execute(sql)        
                for i in db:
                    results.append(i)     
                if results==[]:
                    sql = "INSERT INTO CarUsage(plate,user,start_time,end_time) VALUES ('%s', '%s',  '%s',  '%s')" % (plate,user,start_time,end_time)
                    db.execute(sql)
                    sql = "SELECT * FROM CarUsage order by id_carusage desc limit 1;"
                    db.execute(sql)
                    results=[]
                    for i in db:
                        results.append(i)
                else:
                    results=["Already booked!"] 
        return json.dumps(results, indent=4, sort_keys=True, default=str).encode()

@app.route('/data/carusage/<id>', methods=['PATCH','GET'])
def update_carusage(id):
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:      
        plate = request.values.get("plate")
        user = request.values.get("user")
        start_time = request.values.get("start_time")  
        end_time = request.values.get("end_time")
        results=[] 
        if plate==None or start_time ==None or end_time ==None:
            results=["Please input booking information!"]
        elif is_valid_date(start_time)==False or is_valid_date(end_time)==False:
            results=["Please input right time!"]
        else:
            sql = "UPDATE CarUsage SET plate = '%s', user = '%s', start_time = '%s', end_time = '%s' WHERE id_carusage = '%s'" % (plate,user,start_time,end_time,id)
            db.execute(sql)
            sql = "SELECT * FROM CarUsage WHERE id_carusage = '%s'" % (id)
            db.execute(sql)
            for i in db:
                results.append(i)
        return json.dumps(results, indent=4, sort_keys=True, default=str).encode()

@app.route('/data/carusages/<id>', methods=['DELETE','GET'])
def delete_carusages(id):
    with DB(host='localhost',user='root',passwd='ZAQzaq1234-=',db='TESTDB') as db:
        sql = "DELETE from CarUsage WHERE id_carusage = '%s'" % (id)
        db.execute(sql)
        sql = "SELECT * FROM CarUsage WHERE id_carusage = '%s'" % (id)
        db.execute(sql)
        results=[]
        for i in db:
            results.append(i)
        if results==[]:
            answer=["ok"]
        else:
            answer=["failed"]
        sql = "alter table CarUsage drop column id_carusage;"
        db.execute(sql)
        sql = "alter table CarUsage add id_carusage int not null primary key auto_increment first;"
        db.execute(sql)
        return json.dumps(answer).encode()

def main():
    app.run(host='0.0.0.0',port=8888,debug=True,use_reloader=True)

if __name__ == '__main__':    
      

    main()
 