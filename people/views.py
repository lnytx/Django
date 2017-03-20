from _decimal import Context
from sys import modules

from django.shortcuts import render
from django.template.context_processors import request
from django.views.decorators.csrf import csrf_exempt

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
    return render('insert.html')

#显示数据库数据
def user_list(request):
    people_list=modules.User.object.all()
    #c=Context({'people_list':people_list})
    return render(request,'showuser.html',{'people_list':people_list})
    