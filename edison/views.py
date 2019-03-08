from django.db.models import Q
from django.http import HttpResponseRedirect

from edison.apps import *
from edison.forms import Editacestudenta, Editacepredmetu, Teacher_add, Schedule_add
from edison.models import Student, Subject, Teacher, Schedule
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from edison.apps import *


# Create your views here.
def home(request):
    return render(request, 'edison/home.html')


def admin(request):
    return HttpResponseRedirect('http://localhost:8000/admin/')


def about(request):
    return render(request, 'edison/about.html')


def student(request):
    students = Student.objects.all()
    return render_to_response('edison/student.html', {'students': students})


def studentdetail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render_to_response('edison/studentdetail.html', {'student': student})


def deletestudent(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return HttpResponseRedirect('/student/')


def pridatstudent(request):
    error = ""
    if request.method == "POST":
        form = Editacestudenta(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.login = form.cleaned_data["login"]
            post.name = form.cleaned_data["name"]
            post.surname = form.cleaned_data["surname"]
            post.grade = form.cleaned_data["grade"]
            post.address = form.cleaned_data["address"]
            post.Pass_code = form.cleaned_data["Pass_code"]
            students = Student.objects.all()
            if len(Student.objects.filter(login=post.login)) == 0:
                post.save()
                return HttpResponseRedirect('/student/')
            else:
                error = "Login jiz existuje"
                form = Editacestudenta()
                return render(request, 'edison/editacestudent.html', {'form': form, 'error': error})
        else:
            print('spatne vyplneni')
            return redirect('/pridatstudent/')
    else:
        form = Editacestudenta()
        return render(request, 'edison/editacestudent.html', {'form': form, 'error': error})


def editacestudent(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = Editacestudenta(request.POST, instance=student)
        if form.is_valid():
            post = form.save(commit=False)
            post.login = form.cleaned_data["login"]
            post.name = form.cleaned_data["name"]
            post.surname = form.cleaned_data["surname"]
            post.grade = form.cleaned_data["grade"]
            post.address = form.cleaned_data["address"]
            post.Pass_code = form.cleaned_data["Pass_code"]
            post.save()
            students = Student.objects.all()
            return HttpResponseRedirect('/student/')
        else:
            print('spatne vyplneni')
            return redirect('/student/')
    else:
        form = Editacestudenta(instance=student)
        return render(request, 'edison/editacestudent.html', {'form': form})


def subject(request):
    subjects = Subject.objects.all()
    return render_to_response('edison/subject.html', {'subjects': subjects})


def subjectedit(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    if request.method == "POST":
        form = Editacepredmetu(request.POST, instance=subject)
        if form.is_valid():
            post = form.save(commit=False)
            post.Subject_code = form.cleaned_data["Subject_code"]
            post.Subject_name = form.cleaned_data["Subject_name"]
            post.Subject_points = form.cleaned_data["Subject_points"]
            post.Subject_pass = form.cleaned_data["Subject_pass"]
            post.save()
            subjects = Subject.objects.all()
            return HttpResponseRedirect('/subject/')
        else:
            print('spatne vyplneni')
            return redirect('/subject/')
    else:
        form = Editacepredmetu(instance=subject)
        return render(request, 'edison/subjectedit.html', {'form': form})


def subjectadd(request):
    if request.method == "POST":
        form = Editacepredmetu(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Subject_code = form.cleaned_data["Subject_code"]
            post.Subject_name = form.cleaned_data["Subject_name"]
            post.Subject_points = form.cleaned_data["Subject_points"]
            post.Subject_pass = form.cleaned_data["Subject_pass"]
            post.save()
            return HttpResponseRedirect('/subject/')
        else:
            print('spatne vyplneni')
            return redirect('/pridatpredmet/')
    else:
        form = Editacepredmetu()
        return render(request, 'edison/subjectedit.html', {'form': form})


def subjectdelete(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    subject.delete()
    return HttpResponseRedirect('/subject/')


def teachers(request):
    teachers = Teacher.objects.all()
    return render_to_response('edison/teachers.html', {'teachers': teachers})


def teacheradd(request):
    if request.method == "POST":
        form = Teacher_add(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/teachers/')
        else:
            print('spatne vyplneni')
            return redirect('teacheradd')
    else:
        form = Teacher_add()
        return render(request, 'edison/teacheradd.html', {'form': form})


def teacherdelete(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teacher.delete()
    return HttpResponseRedirect('/teachers/')


def teacherdetail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render_to_response('edison/teacherdetail.html', {'teacher': teacher})


def schedule(request):
    schedules = Schedule.objects.all()
    return render_to_response('edison/schedule.html', {'schedules': schedules})


def scheduledelete(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    schedule.delete()
    return HttpResponseRedirect('/schedule/')


def scheduleadd(request):
    error = ""
    if request.method == "POST":
        form = Schedule_add(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            teachers = Teacher.objects.all()
            control = Teacher.objects.filter(Teacher_name=post.teacher.Teacher_name, Teacher_subject=post.subject)
            if control:
                post.save()
                form.save_m2m()
                return HttpResponseRedirect('/schedule/')
            else:
                error = "Ucitel neuci tento predmet"
                return render(request, 'edison/scheduleadd.html', {'form': form, 'error': error})
        else:
            print('spatne vyplneni')
            return redirect('scheduleadd')

    else:
        form = Schedule_add()
        return render(request, 'edison/scheduleadd.html', {'form': form})
