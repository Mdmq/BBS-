from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.topic, name="topic"),
    path('<int:topic_pk>', views.topic_detail,name="topic_detail"),
    path('type/<int:type_pk>',views.column_all,name="column_all"),
    path('date/<int:year>/<int:month>',views.topics_with_date, name='topics_with_date')
]

