from django.contrib import admin
from . models import *
from imghdr import tests

# Register your models here.

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(test)
admin.site.register(Course)
admin.site.register(StudentProfile)
admin.site.register(EnrolledCourse)