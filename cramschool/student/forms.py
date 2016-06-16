from django import forms
from django.forms.widgets import TextInput
from student.models import Student


class StudentForm(forms.ModelForm):
    sid = forms.CharField(max_length=4, label='學號') #學號
    name = forms.CharField(max_length=10, label='名稱') #名稱
    tel = forms.CharField(max_length=11, label='電話') #電話
    email = forms.CharField(max_length=50, label='電郵') #電郵
    
    class Meta:
        model = Student
        fields = ('sid', 'name', 'tel', 'email')