from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from read_statistics.models import ReadNumExpandMethod

# 用户表
class User(models.Model):
    '''
    用户表
    '''
    uid = models.CharField(verbose_name='电话/用户号', max_length=16, unique=True)
    password = models.CharField(verbose_name='密码', max_length=16,null=True,)
    introduction = models.TextField(blank=True, null=True, verbose_name='简介')
    picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='头像')


class Column(models.Model):
    '''
    版块
    '''
    name = models.CharField(verbose_name='分类名称', max_length=16)
    topic_number = models.IntegerField(default=0)  #主题数

# django 升级到2.0之后,表与表之间关联的时候,必须要写on_delete参数,否则会报异常:
# TypeError: __init__() missing 1 required positional argument: 'on_delete'
    def __str__(self):
        return self.name

class Topic(models.Model,ReadNumExpandMethod):
    '''
    帖子表
    '''
    #标题最大长度30,不能重名
    title=models.CharField(verbose_name='标题',max_length=30,unique=True)
    type=models.ForeignKey(Column,null=True,on_delete=models.CASCADE) #文章类型
    responce_times = models.IntegerField(default=0)  #回复次数
    content = RichTextUploadingField(max_length=150)
    # author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "<topic: %s>" % self.title

    class Meta:
        ordering=['-created_time']





