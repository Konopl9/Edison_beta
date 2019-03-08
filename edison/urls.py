from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from edison import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/$', views.admin,name='admin'),
    url(r'^about/$', views.about, name='about'),
    url(r'^student/$', views.student, name='student'),
    url(r'^student/([0-9]+)$', views.studentdetail, name='studentdetail'),
    url(r'^deletestudent/([0-9]+)$', views.deletestudent,name = 'deletestudent'),
    url(r'^editacestudent/(?P<student_id>[0-9]+)/$', views.editacestudent, name='editacestudent'),
    url(r'^pridatstudent/$', views.pridatstudent, name='pridatstudent'),
    url(r'^subject/$', views.subject, name='subject'),
    url(r'^subjectadd/$', views.subjectadd, name='subjectadd'),
    url(r'^subjectedit/(?P<subject_id>[0-9]+)/$', views.subjectedit, name='subjectedit'),
    url(r'^subjectdelete/([0-9]+)$', views.subjectdelete, name='subjectdelete'),
    url(r'^teachers/$', views.teachers, name='teachers'),
    url(r'^teachers/([0-9]+)$', views.teacherdetail, name='teacherdetail'),
    url(r'^teachersadd/$', views.teacheradd, name='teachersadd'),
    url(r'^teacherdelete/([0-9]+)$', views.teacherdelete, name='teacherdelete'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^scheduleadd/$', views.scheduleadd, name='scheduleadd'),
    url(r'^scheduledelete/([0-9]+)$', views.scheduledelete, name='scheduledelete'),



]
