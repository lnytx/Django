"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
import learn
from learn.views import add2
from people import views as people_views
from django.conf.urls import url, include

urlpatterns = [
    #url(r'^$',learn_views.index),
#     #url(r'^add/$', learn_views.add),
#     url(r'^add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
#     #url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
#     url(r'^$', learn_views.add3,name='home'),
    url(r'^admin/', admin.site.urls),
    #旧页面跳转
#     url(r'^add/(\d+)/(\d+)/$', learn_views.redirect),
#     url(r'^new_add/(\d+)/(\d+)/$',learn_views.add2,name='add2'),
#     url(r'^home/$', learn_views.home),
#     url(r'^list/$', learn_views.for_list),
#     url(r'^dict/$', learn_views.show_dict),
#     url(r'^dict/$', learn_views.show_dict),
#     url(r'^for/$', learn_views.show_for),
#     url(r'^if/$', learn_views.show_if),
#     url(r'^listed/$', learn_views.show_listed),
#    url(r'^people/$', people_views.show_people),
#     url(r'^insert/$',people_views.insert),
#     url(r'^listuser/$',people_views.user_list),
    #url(r'^index/$',people_views.index,name='home'),
    #url(r'^add/$',people_views.add,name='add'),
     url(r'^show/$',people_views.user_list,name='add'),
#按条件导出xls
#     url(r'^ex/$', people_views.export, name='down'),
#     url(r'^id/$', people_views.export_list, name='show'),
#     url(r'^export/$', people_views.xls_mould, name='xls_mould'),
#form表彰
    #url(r'^$', people_views.indexform,name='home1'),
#发送邮件
    url(r'^email_one/$', people_views.email_one, name='email_one'),
    url(r'^email_attch/$', people_views.email_attch, name='email_attch'),
    url(r'^email_html/$', people_views.email_html, name='email_html'),
#用户注册系统
    #url(r'^accounts/', include('users.urls')),
#传数据到js上
    url(r'^js/$', people_views.tra_js, name='tra_js'),
#ajax接收数据
    url(r'^$', people_views.index, name='home'),
    url(r'^ajax/$', people_views.add, name='add'),   
    #ajax接收list与dict数据 
    url(r'^ajax_list_dict/$', people_views.ajax_list_dict, name='home'),
    url(r'^123/$', people_views.ajax_list, name='ajax_list'),
    url(r'^4543/$', people_views.ajax_dict, name='ajax_dict'),
    #url(r'^queryset/$', people_views.queryset, name='ajax_dict'),
#使用上下文渲染（使一个变量在多个模板中使用）
    url(r'^context1/$', people_views.context1),
    url(r'^context2/$', people_views.context2),
#分页的实现
    url(r'^fenye/$', people_views.fenye),
#快递单导出等功能
    url(r'^home/$', people_views.home),
    url(r'^finddelivery/$', people_views.finddelivery,name='finddelivery'),
    url(r'^getresults/', people_views.get_request),
    
]
