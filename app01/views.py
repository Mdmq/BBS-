from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import  Paginator
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db.models import Count
from .models import Column,Topic
from read_statistics.utils import  read_statistics_once_read
from read_statistics.utils import  get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data


# 首页
def home(request):
    topic_content_type=ContentType.objects.get_for_model(Topic)
    dates, read_nums =get_seven_days_read_data(topic_content_type)

    context={}
    context['types']=Column.objects.all()
    context['read_nums']=read_nums
    context['today_hot_data']=get_today_hot_data(topic_content_type)
    context['yesterday_hot_data']=get_yesterday_hot_data(topic_content_type)
    return render(request,'index.html',context)


def get_topic_list_common_data(request, topics_all_list):
    paginator=Paginator(topics_all_list,settings.EACH_PAGE_TOPICS_NUMBER)
    page_num=request.GET.get('page',1)  #获取url的页面参数（get请求)
    page_of_topics=paginator.get_page(page_num)
    page_range=[x for x in range(int(page_num)-2,int(page_num)+3) if 0 < x <= paginator.num_pages]
    #加上省略号
    if page_range[0] - 1 >=2:
        page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1] >=2:
        page_range.append('...')
    #加上首页和尾页
    if page_range[0] !=1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context={}
    context['page_of_topics']=page_of_topics
    context['page_range']=page_range
    context['types']=Column.objects.annotate(topic_count=Count('topic'))
    context['topic_dates']=Topic.objects.dates('created_time','month',order="DESC")
    return context

# 全部帖子
def topic(request):
    topics_all_list = Topic.objects.all()[0:10]
    context=get_topic_list_common_data(request,topics_all_list)
    return render(request,'topic.html',context)

# 所有版块
def column_all(request,type_pk):
    type=get_object_or_404(Column,pk=type_pk)
    topics_all_list = Topic.objects.filter(type=type)

    context=get_topic_list_common_data(request,topics_all_list)
    context['type']=type

    return render(request,'column_all.html',context)

def topics_with_date(request,year,month):
    topics_all_list = Topic.objects.filter(created_time__year=year, created_time__month=month)
    context=get_topic_list_common_data(request,topics_all_list)
    context['topic_with_date']='%s年%s月' % (year, month)

    return render(request,'topics_with_date.html',context)

# 帖子详细
def topic_detail(request,topic_pk):
    topic=get_object_or_404(Topic,pk=topic_pk)
    read_cookie_key=read_statistics_once_read(request,topic)

    context={}
    context['topic']=get_object_or_404(Topic,pk=topic_pk)

    response=render(request,'topic_detail.html',context) #响应
    response.set_cookie(read_cookie_key , 'true')
    return response

'''
    #cookie保存
    response=render(request,'topic_detail.html',context) #响应
    reponse.set_cookie('topic_%s_read' % topic_pk , 'true', max_age=60,expires=datetime)
    return response
'''


'''
def column_detail(request,column_pk): #单个版块
    context={}
    context['column'] = get_object_or_404(Column,pk=column_pk)
    return render('column_detail.html',context)
'''