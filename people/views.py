from _decimal import Context
from _io import StringIO
from audioop import reverse
from sys import modules
import time

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from django.views.decorators.csrf import csrf_exempt
from xlwt import *  
import xlwt

from people.models import User

from .tools import AddForm


# Create your views here.
def show_people(request):
    list3=map(str,range(100))
    return render(request, 'insert.html',{'list3':list3})

#向数据库中插入页面数据
def insert(request):
    if request.method=="POST":
        user=User()
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        user.username=username
        user.password=password
        user.save()
    return render(request,'insert.html')

#显示数据库数据
def user_list(request):
    #people_list=User.objects.all()
    
    #切片操作，获取2个人，不支持负索引，切片可以节约内存
    #people_list=User.objects.all()[:2]
    
    #如果需要获取满足条件的一些人，就要用到filter
    people_list=User.objects.filter(id=3)
    
    #filter是找出满足条件的，当然也有排除符合某条件的
    people_list=User.objects.exclude(id=3)
    people_list=User.objects.filter(id=1).exclude(id=3)
    return render(request,'showuser.html',{'people_list':people_list})



    



#导出xls      
def xls_mould(request):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment; filename='+time.strftime('%Y%m%d',time.localtime(time.time()))+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet(u'订单')
    #1st line   
    sheet.write(0,0, 'id')
    sheet.write(0,1, '用户名')
    sheet.write(0,2, '密码')
    people_list=User.objects.filter(id=items)
   
    row = 1
    for users in people_list:
        sheet.write(row,0, users.id)
        sheet.write(row,1, users.username)
        sheet.write(row,2, users.password)
        row=row + 1
    wb.save(response)    
    return response
        

#页面传值，根据值查询并导出数据
def export(request):
    return render(request, 'items.html')
def export_list(request):
        global items
        items=request.GET.get("id",'None')
        if items=='None':
            item_list=User.objects.all()
        else:
            item_list=User.objects.filter(id=items)
        #return HttpResponse(item_list)
        return render(request,'items.html',{'item_list':item_list})
    
#页面间传值
def index(request):
    return render(request,'index.html')
def add(request):
    a=request.GET.get('a',None)
    b=request.GET.get('b',None)
    a=int(a)
    b=int(b)
    return HttpResponse(str(a+b))

#使用 Django 的 表单 (forms)传值
def indexform(request):
    if request.method=='POST':#当提交表单时
        form=AddForm(request.POST)# form 包含提交的数据
        if form.is_valid():
            #a=int(request.POST.get('a',0))
            #b=int(request.POST['b'])
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:#如果不是post提交数据，就不传参数创建对象，并将对象返回给前台
        form=AddForm()
    return render(request, 'index2.html',{'form':form})

#纯文本发邮件
from django.core.mail import send_mail
def email_one(request):
    send_mail("主题是aaa", "正文是bbb", 'lnytx@163.com', ['lnytx@163.com'], fail_silently=False)
    return HttpResponse('发送成功！')
#有附件的邮件
from django.core.mail import EmailMultiAlternatives
def email_attch(request):
    msg=EmailMultiAlternatives("主题是aaa", "正文是bbb", 'lnytx@163.com', ['lnytx@163.com'])
    msg.attach_file('./aaa.txt','text/html')
    msg.send(fail_silently=False)
    return HttpResponse('发送附件成功！')
#发送html邮件
def email_html(request):
    subject='这是一封信的主题'
    message='这是正文的文本'
    html_content='''
    <p>请输入两个数字社里是get方法</p>
    <form action="/add/" method="get">
    a: <input type="text" name="a"> <br>
    b: <input type="text" name="b"> <br>
    <input type="submit" value="提交">
    <a href="www.baidu.com" ><img src="http://www.divcss5.com/css-images/css-logo.gif" />网络图片</a>
    '''
    msg=EmailMultiAlternatives('subject','message','lnytx@163.com', ['lnytx@163.com'])
    msg.attach_alternative(html_content,'text/html')
    msg.send(fail_silently=True)
    return HttpResponse('发送html附件成功！')
    