from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    scname=models.CharField(max_length=100)
    scprincipal=models.CharField(max_length=100)
    aclocation=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.scname
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Student(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    scname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='balaji')
    def __str__(self) -> str:
        return self.sname