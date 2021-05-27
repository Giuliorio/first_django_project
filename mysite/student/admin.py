from django.contrib import admin

from .models import School, Student, Grade, Faculty, Department, Certificate_type

# Register your models here.

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Certificate_type)