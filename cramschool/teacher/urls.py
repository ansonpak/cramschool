from django.conf.urls import url
from teacher import views


urlpatterns = [
    url(r'^$', views.teacher, name='teacher'),
    url(r'^teacherCreate/', views.teacherCreate, name='teacherCreate'),
    url(r'^teacherSearch/', views.teacherSearch, name='teacherSearch'),
    url(r'^teacherUpdate/(?P<teacherID>\w+)/$', views.teacherUpdate, name='teacherUpdate'),
    url(r'^teacherDelete/(?P<teacherID>\w+)/$', views.teacherDelete, name='teacherDelete'),
]