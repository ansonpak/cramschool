from django import forms
from django.forms.widgets import TextInput
from teacher.models import Teacher


class TeacherForm(forms.ModelForm):
    tid = forms.CharField(max_length=4, label='教師編號') #教師編號
    name = forms.CharField(max_length=10, label='教師名稱') #教師名稱
    subject = forms.ChoiceField(choices=(('國文', '國文'), ('英文', '英文'), ('數學', '數學'), ('理化', '理化'), ('地理', '地理'), ('歷史', '歷史'), ('公民', '公民')), label='教師受教科目') #教師受教科目
    tel = forms.CharField(max_length=11, label='教師電話') #教師電話
    salary = forms.CharField(max_length=50, label='教師薪資') #教師薪資
    
    class Meta:
        model = Teacher
        fields = ('tid', 'name', 'subject', 'tel', 'salary')