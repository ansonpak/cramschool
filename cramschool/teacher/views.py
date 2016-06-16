from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from teacher.forms import TeacherForm
from teacher.models import Teacher
from main.views import paginating, admin_required


def teacher(request):
    teachers = paginating(request, Teacher.objects.all())
    return render(request, 'teacher/teacher.html', {'teachers':teachers})

@admin_required
def teacherCreate(request):
    template = 'teacher/teacherCreate.html'
    if request.method=='GET':
        return render(request, template, {'form':TeacherForm()})
    form = TeacherForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, template, {'form':form})
    teacher = form.save()
    teacher.save()   
    messages.success(request, '師資資料已新增') 
    return redirect(reverse('teacher:teacher'))


def teacherSearch(request):
    searchTerm = request.GET.get('searchTerm')
    teachers = paginating(request, Teacher.objects.filter(Q(tid__icontains=searchTerm) | Q(name__icontains=searchTerm) | Q(tel__icontains=searchTerm) | Q(subject__icontains=searchTerm)))
    return render(request, 'teacher/teacher.html', {'teachers':teachers})


@admin_required
def teacherDelete(request, teacherID):
    if request.method=='GET':
        return teacher(request)
    # POST
    teacher = get_object_or_404(Teacher, tid=teacherID)
    teacher.delete()
    messages.success(request, '師資資料已刪除')
    return redirect('teacher:teacher')

@admin_required
def teacherUpdate(request, teacherID):
    template = 'teacher/teacherUpdate.html'
    teacherToUpdate = get_object_or_404(Teacher, tid=teacherID)
    if request.method=='GET':            
        form = TeacherForm(instance=teacherToUpdate)
        return render(request, template, {'form':form, 'teacher':teacherToUpdate})
    # POST
    form = TeacherForm(request.POST, instance=teacherToUpdate)
    if not form.is_valid():
        return render(request, template, {'form':form, 'teacher':teacherToUpdate})
    teacher=form.save()
    messages.success(request, '師資資料已修改')
    return redirect('teacher:teacher')