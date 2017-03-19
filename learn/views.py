#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from builtins import int, str
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import request
# Create your views here.
def index(request):
    return HttpResponse(u'第一个项目')
def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(str(c))
def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
#这里使用了模板及渲染技术
def add3(request):
    return render(request,'home.html')
#将用户收藏夹中的旧地址跳转到现在的新网址
def redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
        )

#在视图中我们传递了一个字符串名称是 string 到模板 home.html，
def home(request):
    string=u"我在学习Django在用它来建网站"
    return render(request, 'home.html', {'string': string})




    