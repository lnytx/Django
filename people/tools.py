# -*- coding:utf-8 -*-
'''
Created on 2017年3月21日

@author: admin
'''
from django import forms


class AddForm(forms.Form):
    a=forms.IntegerField()
    b=forms.IntegerField()
