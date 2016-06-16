from django import forms
from django.forms.widgets import TextInput
from courses.models import Courses
from student.models import Student
from teacher.models import Teacher
from scores.models import Scores


class ScoresForm(forms.ModelForm):
    sid = forms.ModelChoiceField(queryset=Student.objects.all(), label='學生編號') #學生編號
    tid = forms.ModelChoiceField(queryset=Teacher.objects.all(), label='教師編號') #教師編號
    cid = forms.ModelChoiceField(queryset=Courses.objects.all(), label='課堂編號') #課堂編號
    scid = forms.CharField(max_length=4, label='成績編號') #成績編號
    score = forms.CharField(label='成績') #成績
    
    
    class Meta:
        model = Scores
        fields = ('sid', 'tid', 'cid', 'scid', 'score')