from django.db import models

# Create your models here.
class Scores(models.Model):
    sid = models.CharField(max_length=128)
    tid = models.CharField(max_length=128)
    cid = models.CharField(max_length=128)
    scid = models.CharField(max_length=128, primary_key=True)
    score = models.CharField(max_length=128)
    
    def __str__(self):
        return self.scid
    
    class Meta:
        managed = False
        db_table = 'SCORESDB'