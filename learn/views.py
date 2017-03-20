#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from builtins import int, str
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import request
from idlelib.idle_test.mock_tk import Var
from idlelib.WindowList import ListedToplevel
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

#在视图中我们传递了一个List到模板 home.html，在模板中这样使用它：
def for_list(request):
    list1=['a','b','jack','tom','tiiger']
    return render(request, 'home.html',{'list':list1})

#显示字典中内容
def show_dict(request):
    dictname={'site':u'学习Django','content':u'各个IT技术'}
    return render(request,'home.html',{'dict':dictname})
#在模板进行 条件判断和 for 循环的详细操作
def show_for(request):
    list2=map(str,range(100))
    return render(request, 'home.html',{'list2':list2})

#使用if
def show_if(request):
    var=76
    return render(request, 'home.html',{'var':var})
def show_listed(request):
    listed=[['a','b'],['c','d']]
    return render(request, 'home.html',{'listed':listed})
    