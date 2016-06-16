from django.conf.urls import url
from scores import views


urlpatterns = [
    url(r'^$', views.scores, name='scores'),
    url(r'^scoresCreate/', views.scoresCreate, name='scoresCreate'),
    url(r'^scoresSearch/', views.scoresSearch, name='scoresSearch'),
    url(r'^scoresUpdate/(?P<scoresID>\w+)/$', views.scoresUpdate, name='scoresUpdate'),
    url(r'^scoresDelete/(?P<scoresID>\w+)/$', views.scoresDelete, name='scoresDelete'),
]