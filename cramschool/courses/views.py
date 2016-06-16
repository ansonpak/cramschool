from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from courses.forms import CoursesForm
from courses.models import Courses
from main.views import paginating, admin_required


def courses(request):
    coursess = paginating(request, Courses.objects.all())
    return render(request, 'courses/courses.html', {'coursess':coursess})

@admin_required
def coursesCreate(request):
    template = 'courses/coursesCreate.html'
    if request.method=='GET':
        return render(request, template, {'form':CoursesForm()})
    form = CoursesForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, template, {'form':form})
    courses = form.save()
    courses.save()   
    messages.success(request, '師資資料已新增') 
    return redirect(reverse('courses:courses'))


def coursesSearch(request):
    searchTerm = request.GET.get('searchTerm')
    coursess = paginating(request, Courses.objects.filter(Q(tid__icontains=searchTerm) | Q(cid__icontains=searchTerm) | Q(title__icontains=searchTerm) | Q(time__icontains=searchTerm) | Q(classroom__icontains=searchTerm) | Q(price__icontains=searchTerm)))
    return render(request, 'courses/courses.html', {'coursess':coursess})


@admin_required
def coursesDelete(request, coursesID):
    if request.method=='GET':
        return courses(request)
    # POST
    courses = get_object_or_404(Courses, cid=coursesID)
    courses.delete()
    messages.success(request, '師資資料已刪除')
    return redirect('courses:courses')

@admin_required
def coursesUpdate(request, coursesID):
    template = 'courses/coursesUpdate.html'
    coursesToUpdate = get_object_or_404(Courses, cid=coursesID)
    if request.method=='GET':            
        form = CoursesForm(instance=coursesToUpdate)
        return render(request, template, {'form':form, 'courses':coursesToUpdate})
    # POST
    form = CoursesForm(request.POST, instance=coursesToUpdate)
    if not form.is_valid():
        return render(request, template, {'form':form, 'courses':coursesToUpdate})
    courses=form.save()
    messages.success(request, '師資資料已修改')
    return redirect('courses:courses')