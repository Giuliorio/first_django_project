from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 400)

    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length = 1)

    def __str__(self):
        return self.name


class Certificate_type(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length = 50)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Student(models.Model):
        school = models.ForeignKey(School, on_delete=models.PROTECT, default = 0)
        first_name = models.CharField(max_length = 50)
        last_name = models.CharField(max_length = 50)
        age = models.IntegerField()
        department = models.ForeignKey(Department, on_delete=models.PROTECT)
        grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
        certificate_type = models.ForeignKey(Certificate_type, on_delete=models.PROTECT)

        def __str__(self):
            return self.first_name
