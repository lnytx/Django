'''
Created on 2017年3月25日

@author: admin
'''
from django.template.context_processors import request
'''
再比如，我们在网站放到服务器上正式运行后，DEBUG改为了 False，这样更安全，但是有时候发生错误我们不能看到错误详情，调试不方便，有没有办法处理好这两个事情呢？

普通访问者看到的是友好的报错信息

管理员看到的是错误详情，以便于修复 BUG

当然可以有，利用中间件就可以做到！代码如下：
'''
import sys
from django.views.debug import technical_500_response
from django.conf import settings
 
class UserBasedExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_500_response(request, *sys.exc_info())
        
        
 
