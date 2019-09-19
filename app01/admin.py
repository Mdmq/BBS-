from django.contrib import admin
from .models import Column,Topic

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title','type','content','get_read_num','created_time','responce_times',)

# @admin.register(ReadNum)
# class ReadNumAdmin(admin.ModelAdmin):
#     list_display = ('read_num','topic',)