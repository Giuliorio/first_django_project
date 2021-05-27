from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 400)

class Grade(models.Model):
    type = models.IntegerField()

class Certificate_type(models.Model):
    name = models.CharField(max_length = 50)

class Faculty(models.Model):
    name = models.CharField(max_length = 50)

class Department(models.Model):
    name = models.CharField(max_length = 50)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

class Student(models.Model):
        school = models.ForeignKey(School, on_delete=models.PROTECT, default = 0)
        first_name = models.CharField(max_length = 50)
        last_name = models.CharField(max_length = 50)
        age = models.IntegerField()
        department = models.CharField(max_length = 50)
        grade = models.ForeignKey(Grade, on_delete=models.PROTECT)
        certificate_type = models.CharField(max_length = 50)  