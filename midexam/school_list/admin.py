from django.contrib import admin
from school_list.models import Student
from school_list.models import Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)