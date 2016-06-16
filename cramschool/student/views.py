from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect, get_object_or_404
from main.views import admin_required, manager_required, paginating
from student.forms import StudentForm
from student.models import Student


def student(request):
    #if request.user.username[0] == 'S':
        #students = paginating(request, Student.objects.filter(sid = request.user.username))
        #return render(request, 'student/student.html', {'students':students})
    students = paginating(request, Student.objects.all())
    return render(request, 'student/student.html', {'students':students})

@admin_required
def studentCreate(request):
    template = 'student/studentCreate.html'
    if request.method=='GET':
        return render(request, template, {'form':StudentForm()})
    form = StudentForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, template, {'form':form})
    student = form.save()
    student.save()
    messages.success(request, '學生資料已新增')
    return redirect(reverse('student:student'))


def studentSearch(request):
    searchTerm = request.GET.get('searchTerm')
    students = paginating(request, Student.objects.filter(Q(sid__icontains=searchTerm) | Q(name__icontains=searchTerm) | Q(tel__icontains=searchTerm) | Q(email__icontains=searchTerm)))
    return render(request, 'student/student.html', {'students':students})


@admin_required
def studentDelete(request, studentID):
    if request.method=='GET':
        return student(request)
    # POST
    student = get_object_or_404(Student, sid=studentID)
    student.delete()
    messages.success(request, '學生資料已刪除')
    return redirect('student:student')

@admin_required
def studentUpdate(request, studentID):
    template = 'student/studentUpdate.html'
    studentToUpdate = get_object_or_404(Student, sid=studentID)
    if request.method=='GET':            
        form = StudentForm(instance=studentToUpdate)
        return render(request, template, {'form':form, 'student':studentToUpdate})
    # POST
    form = StudentForm(request.POST, instance=studentToUpdate)
    if not form.is_valid():
        return render(request, template, {'form':form, 'student':studentToUpdate})
    student=form.save()
    messages.success(request, '學生資料已修改')
    return redirect('student:student')