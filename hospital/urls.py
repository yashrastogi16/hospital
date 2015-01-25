from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/','login.views.base',name='base'),
    url(r'^$','login.views.home',name='home'),
    url(r'^home/','login.views.home',name='home'),
    url(r'^registerpatient/','login.views.registerpatient',name='registerpatient'),
    url(r'^patientrecord/','login.views.patientrecord',name='patientrecord'),
    url(r'^managepatient/','login.views.managepatient',name='managepatient'),
    url(r'^admin_login/','login.views.login',name='login'),
    url(r'^logout/','login.views.logout',name='logout'),
    url(r'^register/','login.views.adminregister',name='adminregister'),
    url(r'^individual/','login.views.individual',name='individual'),
)
