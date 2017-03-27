# -*-coding:utf-8 -*-
'''
Created on 2017年3月25日
动手写个上下文渲染器
把一个变量在多个模板之间共用，这时候就可以用 Django 上下文渲染器。
@author: admin
'''
from django.conf import settings as original_settings

from mysite.settings import BASE_DIR


def settings(request):
    return {'settings': original_settings}

def ip_address(request):
    return {'ip_address':request.META['REMOTE_ADDR']}

print(BASE_DIR)