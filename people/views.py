from _decimal import Context
from _io import StringIO
from _pickle import dumps
from audioop import reverse
import json
from sys import modules
import time

from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponse, JsonResponse
from xlwt import *  
import xlwt

from people.connect_mysql import *

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
    people_list=User.objects.all()
    
#     #切片操作，获取2个人，不支持负索引，切片可以节约内存
#     #people_list=User.objects.all()[:2]
#     
#     #如果需要获取满足条件的一些人，就要用到filter
#     people_list=User.objects.filter(id=3)
#     
#     #filter是找出满足条件的，当然也有排除符合某条件的
#     people_list=User.objects.exclude(id=3)
#     people_list=User.objects.filter(id=1).exclude(id=3)
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
    
#页面间传值（以及ajax接收数据）
def index(request):
    return render(request,'ajax.html')
def add(request):
    a=request.GET.get('a',None)
    b=request.GET.get('b',None)
    a=int(a)
    b=int(b)
    #return HttpResponse(str(a+b))
    #下面这个是测试ajax的
    list=['django','渲染json到模板']
    dict={'site':'王二小','author':'无名'}
    #ajax可以传这些查询数据库数据到前台页面中
    #people_list=User.objects.all()
    people_list=User.objects.filter(id=1)
    #return HttpResponse(people_list.username)
    return HttpResponse(str(int(a)+int(b)))


##页面间传值（向前台传输list与dict）
#向前台传输list列表
def ajax_list_dict(request):
    return render(request,'ajax_list_dict.html')
def ajax_list(request):
    list=[x for x in range(100)]
    #a=['a','b','c','d','e']
    #return HttpResponse(json.dumps(a), content_type='application/json')
#向前台传输dict
def ajax_dict(request):
    dict={'name':'人名','age':15,'班级':'高三(3)班','分数':99}
    #return HttpResponse(json.dumps(dict),content_type=('application/json')
    return JsonResponse(dict)
#为user对象自定义一个方法来初现将user对象序列化，否则不能序列化
# def user2dict(user):
#     return {
#         #'id': user.id,
#         'name': user.username,
#         'pass': user.password
#     }
# def queryset(request):
#     people_list=User.objects.all()
#     return  HttpResponse(json.dumps(people_list,default=user2dict),content_type=('application/json'))



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
    #return render(request, 'index2.html',{'form':form})


#纯文本发邮件
def email_one(request):
    send_mail("主题是aaa", "正文是bbb", 'lnytx@163.com', ['lnytx@163.com'], fail_silently=False)
    return HttpResponse('发送成功！')
#有附件的邮件
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
    
    #Django传递数据给JS
def tra_js(request):
    list=['django','渲染json到模板']
    dict={'site':'王二小','author':'无名'}
    return render(request, 'js.html', {
        'List': json.dumps(list),
        'Dict': json.dumps(dict)
    })
    return render(request, 'js.html', {'List':json.dumps(list),'Dict':json.dumps(dict)})

#动手写个上下文渲染器
#把一个变量在多个模板之间共用，这时候就可以用 Django 上下文渲染器。
#1、建渲染的模板，此例是context_processor.py模板，2、将新建的模板放入settings.py中3、修改views.py与urls.py
def context1(request):
    return render(request,'context1.html')
def context2(request):
    return render(request,'context2.html')


######
######分页功能实现（根据订单号查找快递单号，并显示到finddelivery.html）
def rev(request):
    list_orders=[]
    list_orders=request.GET().get('a','None')
    request.GET.get("id",'None')
def fenye(request):
    user_list = select_table()
    page = request.GET.get('page',1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, './worker/fenye.html', { 'users': users })
