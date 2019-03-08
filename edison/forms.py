from django import forms
from .models import Student, Subject, Teacher, Schedule


class Editacestudenta(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('login', 'name', 'surname', 'mail', 'grade', 'address', 'Pass_code')


class Editacepredmetu(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('Subject_code', 'Subject_name', 'Subject_points', 'Subject_pass')


class Teacher_add(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('Teacher_name', 'Teacher_surname', 'Teacher_subject')


class Schedule_add(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('subject', 'teacher', 'times', 'days', 'students')
