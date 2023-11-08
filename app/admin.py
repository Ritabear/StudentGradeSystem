from django.contrib import admin

# Register your models here.
from .models import Student, Subject, Grade

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)