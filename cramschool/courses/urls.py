from django.conf.urls import url
from courses import views


urlpatterns = [
    url(r'^$', views.courses, name='courses'),
    url(r'^coursesCreate/', views.coursesCreate, name='coursesCreate'),
    url(r'^coursesSearch/', views.coursesSearch, name='coursesSearch'),
    url(r'^coursesUpdate/(?P<coursesID>\w+)/$', views.coursesUpdate, name='coursesUpdate'),
    url(r'^coursesDelete/(?P<coursesID>\w+)/$', views.coursesDelete, name='coursesDelete'),
]