"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("student_register",views.student_register,name="student_register"),
    path("logins",views.logins,name="logins"),
    path("adminhome",views.adminhome,name="adminhome"),
    path("teacher_reg",views.teacher_reg,name="teacher_reg"),
    path("studentview",views.studentview,name="studentview"),
    path("studentdelete/<int:id>",views.studentdelete,name="studentdelete"),

    path("studentedit",views.studentedit,name="studentedit"),

    path("studentupdate/<int:id>",views.studentupdate,name="studentupdate"),

    path("studentapprove/<int:id>",views.studentapprove,name="studentapprove"),

    path("studenthome",views.studenthome,name="studenthome"),

    path("studentdata",views.studentdata,name="studentdata"),

    path("teacherview",views.teacherview,name="teacherview"),

    path("teacherdelete/<int:id>",views.teacherdelete,name="teacherdelete"),
 
    path("teacheredit",views.teacheredit,name="teacheredit"),

    path("teacherhome",views.teacherhome,name="teacherhome"),

    path("teacherupdate/<int:id>",views.teacherupdate,name="teacherupdate"),

    path("logouts",views.logouts,name="logouts"),
    
    path("logouts",views.logouts,name="logouts"),

    path('index',views.index,name='index')


]
