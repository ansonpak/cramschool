from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    tel = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    
    def __str__(self):
        return self.sid
    
    class Meta:
        managed = False
        db_table = 'STUDENTSDB'