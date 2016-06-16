from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^student/', include('student.urls', namespace='student')),
    url(r'^teacher/', include('teacher.urls', namespace='teacher')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^scores/', include('scores.urls', namespace='scores')),
]