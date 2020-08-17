from django.db import models

class SubjectModel(models.Model):
    classid=models.IntegerField(primary_key=True)
    subject=models.CharField(max_length=30)

class StudentModel(models.Model):
    studentid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField(default=True)
    subject=models.ManyToManyField(SubjectModel)
