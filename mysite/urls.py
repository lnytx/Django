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

urlpatterns = [
    #url(r'^$',learn_views.index),
    #url(r'^add/$', learn_views.add),
    url(r'^add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    #url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^$', learn_views.add3,name='home'),
    #url(r'^admin/', admin.site.urls),
    #旧页面跳转
    url(r'^add/(\d+)/(\d+)/$', learn_views.redirect),
    url(r'^new_add/(\d+)/(\d+)/$',learn_views.add2,name='add2'),
    url(r'^home/$', learn_views.home),
    url(r'^list/$', learn_views.for_list),
    url(r'^dict/$', learn_views.show_dict),
    url(r'^dict/$', learn_views.show_dict),
    url(r'^for/$', learn_views.show_for),
    url(r'^if/$', learn_views.show_if),
    url(r'^listed/$', learn_views.show_listed),
    url(r'^people/$', people_views.show_people),
    url(r'^insert/$',people_views.insert),
    url(r'^listuser/$',people_views.user_list),
    url(r'^id/$', people_views.export, name='export'),
    url(r'^importmould/$', people_views.xls_mould, name='xls_mould'),
]
