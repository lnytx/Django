#-*-coding:utf-8-*-
'''
Created on 2017年3月27日

@author: admin
'''
from django.shortcuts import render
from mysql.connector import cursor
import mysql.connector

from people.models import User


def connect():
    config={'host':'127.0.0.1',
                'user':'root',
                'password':'root',
                'port':3306,
                'database':'pythontest',
                'charset':'utf8'
            }
    try:
        conn=mysql.connector.connect(**config)
        return conn
        print("conn is success!")
    except mysql.connector.Error as e:
        print("conn is fails{}".format(e))
        
def select_table():
    sql_select='select * from test'
    result=[]
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql_select)
        result = cursor.fetchall()#queryset返回列表
#         for id,name,age,commen in cursor:
#             result.append(id)
#             result.append(name)
#             result.append(age)
#             result.append(commen)
        print(result)
        return result
    except mysql.connector.Error as e:
        print("select cursor is faild".format(e))
select_table()

