from django.db import models

# Create your models here.
class student(models.Model):
    cNumber = models.CharField(max_length=9, null=False)
    cName = models.CharField(max_length=5, null=False)
    cMajor = models.CharField(max_length=3, null=False)
    cGrade = models.CharField(max_length=2, null=False)
    ctime = models.CharField(max_length=13, blank=True, default='')
    cMail = models.EmailField(max_length=35, null=False, default='')
    cStatus = models.CharField(max_length=4, blank=True, default='尚未進場')
    def __str__(self):
        return self.cName