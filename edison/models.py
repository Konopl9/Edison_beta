from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


# Create your models here.
class Student(models.Model):
    login = models.CharField(max_length=7)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    grade = IntegerRangeField(min_value=1, max_value=5)
    address = models.CharField(max_length=100)
    Pass_code = models.CharField(max_length=13)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        verbose_name_plural = 'Student'


class Subject(models.Model):
    Passes = (
        (1, 'Examination'),
        (2, 'Credit'),
    )
    Subject_code = models.CharField(max_length=20)
    Subject_name = models.CharField(max_length=50)
    Subject_points = IntegerRangeField(min_value=1, max_value=15)
    Subject_pass = models.IntegerField(choices=Passes)

    def __str__(self):
        return self.Subject_name

    class Meta:
        verbose_name_plural = 'Subject'


class Teacher(models.Model):
    Teacher_name = models.CharField(max_length=20)
    Teacher_surname = models.CharField(max_length=20)
    Teacher_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.Teacher_name + " " + self.Teacher_surname

    class Meta:
        verbose_name_plural = 'Teachers'


class Schedule(models.Model):
    TIMES = (
        ('7:00-8:45', '7:00-8:45'),
        ('9:00-10:30', '9:00-10:30'),
        ('10:45-12:15', '10:45-12:15'),
        ('12:30-14:00', '12:30-14:00'),
        ('12:30-14:00', '12:30-14:00'),
        ('14:15-15:45', '14:15-15:45'),
        ('16:00-17:30', '16:00-17:30'),
    )
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    times = models.CharField(max_length=30, choices=TIMES)
    days = models.CharField(max_length=30, choices=DAYS)
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return str(self.subject) + " " + str(self.times)
