from django.db import models


# Create your models here.
class Courses(models.Model):
    tid = models.CharField(max_length=128)
    cid = models.CharField(max_length=128, primary_key=True)
    title = models.CharField(max_length=128)
    time = models.CharField(max_length=128)
    classroom = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    
    def __str__(self):
        return self.cid
    
    class Meta:
        managed = False
        db_table = 'COURSESDB'