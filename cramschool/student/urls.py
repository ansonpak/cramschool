from django.conf.urls import url
from student import views


urlpatterns = [
    url(r'^$', views.student, name='student'),
    url(r'^studentCreate/', views.studentCreate, name='studentCreate'),
    url(r'^studentSearch/', views.studentSearch, name='studentSearch'),
    url(r'^studentUpdate/(?P<studentID>\w+)/$', views.studentUpdate, name='studentUpdate'),
    url(r'^studentDelete/(?P<studentID>\w+)/$', views.studentDelete, name='studentDelete'),
]