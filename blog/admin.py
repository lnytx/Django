#-*-coding:utf-8-*-
from django.contrib import admin


from .models import Article,Person


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    #搜索功能：search_fields = ('title', 'content',) 这样就可以按照 标题或内容搜索了
    search_fields = ('title', 'content',)
    #筛选功能：list_filter = ('status',) 这样就可以根据文章的状态去筛选，比如找出是草稿的文章
    list_filter = ('title',)
    list_display=('title','pub_date','update_time')

    
#定制搜索功能（django 1.6及以上才有)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name',)
    ##修改保存时的一些操作，可以检查用户，保存的内容等，比如保存时加上添加人
    def save_model(self, request, obj, form, change):
        if change:# 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:# 新增的时候
            obj_original = None
        obj.user = request.user
        obj.save()
    #删除时做的一些处理
    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        # handle something here
        obj.delete()
    #定制搜索功能
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct
#定制加载的列表, 根据不同的人显示不同的内容列表，比如输入员只能看见自己输入的，审核员能看到所有的草稿   
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
list_filter = ('title',) 
