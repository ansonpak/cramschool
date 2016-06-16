from django import forms
from django.forms.widgets import TextInput
from courses.models import Courses
from teacher.models import Teacher


class CoursesForm(forms.ModelForm):
    tid = forms.ModelChoiceField(queryset=Teacher.objects.all(), label='教師編號') #教師編號
    cid = forms.CharField(max_length=4, label='課堂編號') #課堂編號
    title = forms.CharField(max_length=10, label='課堂名稱') #課堂名稱
    time = forms.CharField(label='課堂時間') #課堂時間
    classroom = forms.CharField(max_length=11, label='授課教室') #授課教室
    price = forms.CharField(max_length=50, label='課堂價錢') #課堂價錢
    
    class Meta:
        model = Courses
        fields = ('tid', 'cid', 'title', 'time', 'classroom', 'price')