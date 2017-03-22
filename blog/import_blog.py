#-*- coding:utf-8 -*-
'''
Created on 2017年3月22日

@author: ning.lin
'''
import os

import django


#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if django.VERSION >= (1, 7):
    django.setup()

def main():
    print(BASE_DIR)
    from blog.models import Article
    #art=Article()
    f=open('import1.txt','r')
    
    for line in f:
        if not line.find("#")==-1:#如果找到了#号才执行下面的，否则不执行
            title,content,pub_date,update_time=line.split('#')
            #ValueError: need more than 1 value to unpack
            #可以发现这句话里面并没有#号，而我们要#号进行拆分,本文是因为后面有多个空行
            print(title,content,pub_date,update_time)
    #         art.title=title
    #         art.content=content
    #         art.pub_date=pub_date
    #         art.update_time=update_time
    #         art.save()
            Article.objects.create(title=title,content=content,pub_date=pub_date,update_time=update_time)
            #下面这条不会重复导入
            Article.objects.get_or_create(title=title,content=content,pub_date=pub_date,update_time=update_time)
    f.close()
#使用Model.objects.bulk_create()方式
def b():
    from blog.models import Article
    f=open('import1.txt','r') 
    Blog_List=[]
    for line in f:
        if not line.find("#")==-1:
            title,content,pub_date,update_time=line.split('#')
            art=Article(title=title,content=content,pub_date=pub_date,update_time=update_time)
            Blog_List.append(art)
            print(Blog_List)
            #而bulk_create()是执行一条SQL存入多条数据，做会快很多！
            Article.objects.bulk_create(Blog_List)
    f.close()
#用列表解析代替 for 循环会更快
def c():
    from blog.models import Article
    f=open('import1.txt','r') 
    Blog_List=[]
    # 以下四行 也可以用 列表解析 写成下面这样
    # BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]
    for line in f:
        if not line.find("#")==-1:
            parts=line.split('#')
            art=Article(title=parts[0],content=parts[1],pub_date=parts[2],update_time=parts[3])
            Blog_List.append(art)
            print(Blog_List)
            #而bulk_create()是执行一条SQL存入多条数据，做会快很多！
            Article.objects.bulk_create(Blog_List)
    f.close()
if __name__=="__main__":
    #main()
    #b()
    c()
    print("done")
    