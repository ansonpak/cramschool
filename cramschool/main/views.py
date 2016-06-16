from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.utils import ErrorList
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from cramschool.settings import LOGIN_URL
from student.models import Student
from teacher.models import Teacher


def main(request):
    #user = User.objects.create(username=Student.objects.get.sid, password=Student.objects.get.sid, email=None)
    #staff = User.objects.create(username=Teacher.objects.get(tid), password=Teacher.objects.get(tid), email=None, is_staff=True)
    return render(request, 'main/main.html')


def admin_required(fun):
    def auth(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(LOGIN_URL)
        if request.user.username!='admin':
            messages.error(request, _('沒有權限'))
            return render(request, 'main/main.html')
        return fun(request, *args, **kwargs)
    return auth

def manager_required(fun):
    def auth(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(LOGIN_URL)
        if request.user.userProfile.position!='manager':
            return render(request, 'main/main.html')
        return fun(request, *args, **kwargs)
    return auth


class ErrorMessage(ErrorList):
    def __str__(self):
        return ', '.join([e for e in self])


def paginating(request, objects, objectsPerPage=10):
    paginator = Paginator(objects, objectsPerPage)
    page = request.GET.get('page')
    try:
        objectsList = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objectsList = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objectsList = paginator.page(paginator.num_pages)
    return objectsList