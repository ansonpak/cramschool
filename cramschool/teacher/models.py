from django.db import models

# Create your models here.
class Teacher(models.Model):
    tid = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    tel = models.CharField(max_length=128)
    salary = models.CharField(max_length=128)
    
    def __str__(self):
        return self.tid
    
    class Meta:
        managed = False
        db_table = 'TEACHERSDB'