#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from builtins import int, str
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
    return render(request,u'home.html'.encode(encoding='utf_8', errors='strict'))
#将用户收藏夹中的旧地址跳转到现在的新网址
def redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
        )







    