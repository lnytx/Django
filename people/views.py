from _decimal import Context
from _io import StringIO
from audioop import reverse
from sys import modules

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from django.views.decorators.csrf import csrf_exempt
from xlwt import *  
import xlwt

from people.models import User


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

#导出数据
def export(request):
#     if request=='POST':
#         if request.POST.has_key("export"):
        items=request.POST.get("id",None)
        item_list=User.objects.filter(id=items)
        return render(request,'items.html',{'list':item_list})
#         return HttpResponseRedirect(
#             reverse('down')
#             )




        
def xls_mould(request):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment; filename=DEMO.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet(u'订单')
    #1st line   
    sheet.write(0,0, 'id')
    sheet.write(0,1, '用户名')
    sheet.write(0,2, '密码')
    
    people_list=User.objects.all()
   
    row = 1
    for users in people_list:
        sheet.write(row,0, users.id)
        sheet.write(row,1, users.username)
        sheet.write(row,2, users.password)
        row=row + 1
    wb.save(response)    
    return response
        