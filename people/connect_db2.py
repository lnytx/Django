#  
# #-*-coding:utf-8-*- 
# '''
# Created on 2017年3月27
# 
# @author: ning.lin
# '''
# 
# 
# 
# import datetime
# import string
# import time
# 
# from django import db
# import ibm_db
# import ibm_db_dbi
# import ibm_db_django
# import ibm_db_dlls
# from pip._vendor.requests.packages.urllib3.connectionpool import xrange
# import xlwt
# 
# 
# #maintain/OCH2012ujm
# #DB2INST1
# conn = ibm_db_dbi.connect("PORT=50000;PROTOCOL=TCPIP;", host="10.0.12.115",database="TRENDYEC", user="maintain",password="OCH2012ujm")
# #conn = ibm_db_dbi.connect("DATABASE=DB2INST1;HOSTNAME=10.0.12.115;PORT=50000;PROTOCOL=TCPIP;UID=maintain;PWD=OCH2012ujm;", "", "")
# #conn.set_autocommit(True)#设置自动提交
# 
# cursor = conn.cursor()
# #sql = "select orders_id from DB2INST1.orders where orders_id='11566785'"
# #result = cursor.execute(sql)
# orders_id=11566785
# args=(11579261,
# 11578781,
# 11578782,
# 11579278,
# 11578803,
# 11579843,
# 11579845,
# 11579847)
# 
# 
# def format(args):
#     s=''
#     for a in args:
#         s=s+'%s,'
#     print(s)
#     print('('+ s[:-1]+ ')')
#     return '('+ s[:-1]+ ')'
# format(args)
# #sql1='select * from DB2INST1.orders where orders_id in'+format(args) % tuple(args)
#  
# 
# 
# sql2='''
# select a.orders_id,b.ormorder,a.field2,a.field3,a.field4,a.field5 from  
# DB2INST1.xordextdata a,DB2INST1.orders b where a.orders_id=b.orders_id and a.orders_id in
# ''' +format(args) % tuple(args)
# print(sql2)
#  
# cursor.execute(sql2)
# rows = cursor.fetchall()
# print("查询结果",rows)
# def task_time(formattime):
#     t1=str(formattime)[20:31]
#     t2=str(formattime)[33:42]
#     t=t1.replace(', ', '-')+' '+t2.replace(', ', ':')
#     return t
# 
# workbook = xlwt.Workbook()
# sheet = workbook.add_sheet('orders')
# # style = xlwt.XFStyle()
# # style.num_format_str = 'YY/M/D h:mm:ss' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
# row = 1
# j=0
# for i in xrange(len(rows)):
#     for j in xrange(len(rows[i])):
#         print(rows[0][0])
#         print(rows[0][1])
#         sheet.write(i,j, rows[i][j])
#     row=row + 1
# try:
#     workbook.save('1.xls')
# except IOError as e:
#     print(e)