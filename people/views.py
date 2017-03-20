from django.shortcuts import render

from sys import modules
from django.template.context_processors import request
from _decimal import Context


# Create your views here.
def show_people(request):
    list3=map(str,range(100))
    return render(request, 'insert.html',{'list3':list3})

#向数据库中插入页面数据
def insert(request):
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        modules.User.objects.create(username=username,password=password)
        modules.User.save()
    return render(request,'insert.html')

#显示数据库数据
def user_list(request):
    people_list=modules.User.object.all()
    #c=Context({'people_list':people_list})
    return render(request,'showuser.html',{'people_list':people_list})
    