from django.contrib import admin

# Register your models here.
from edison.models import Student, Subject, Teacher, Schedule

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Schedule)
