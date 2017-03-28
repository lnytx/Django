#-*-coding:utf-8-*-
'''
Created on 2017年3月27日

@author: admin
'''
import mysql.connector





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

def task_time(formattime):
    t1=str(formattime)[20:31]
    t2=str(formattime)[33:42]
    t=t1.replace(', ', '-')+' '+t2.replace(', ', ':')
    return t

def format_args(args):
    s=''
    for a in args:
        s=s+'%s,'
    #print(s)
    #print('('+ s[:-1]+ ')')
    return '('+ s[:-1]+ ')'
# print("aa")
# 
# sql1='select * from test where id in'+format(args) % tuple(args)
# print("sql1",sql1)
def select_table(sql):
    #sql_select='select * from test'
    result=[]
    try:
        conn=connect()
        cursor=conn.cursor()
        cursor.execute(sql)
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

# def main():
#     print("aaaaa",format_args(args))  
# if __name__ == '__main__':
#     main()