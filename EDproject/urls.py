"""EDproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from EDApp import views
from django.urls import include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupPage),
    path('', views.HomePage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.AdminHomePage),
    path('info/', views.Instituteinfo.as_view(),name='homeinstitute'),
    path('updateinfo/<pk>', views.Updateinfo.as_view()),
    path('allclasses/', views.AllClasses.as_view(),name='homeclass'),
    path('newclass/', views.NewClass.as_view()),
    path('editclass/', views.EditClass),
    path('updateclass/<pk>', views.UpdateClass.as_view()),
    path('delete/<pk>', views.DeleteClass.as_view()),
    path('addsubjects/', views.AddSubjects.as_view()),
    path('subjectstoclasses/', views.SubjectstoClasses.as_view()),
    path('allstudents/', views.AllStudents.as_view(),name='homestudent'),
    path('newstudent/', views.NewStudent.as_view()),
    path('deletestudent/<pk>', views.DeleteStudent.as_view()),
    path('updatestudent/<pk>', views.UpdateStudent.as_view()),
    path('admissionletter/', views.AdmissionLetter.as_view()),
    path('printletter/<pk>',views.PrintDetail.as_view()),
    path('allemployees/',views.AllEmployees.as_view(),name='homeemployee'),
    path('newemployee/',views.NewEmployees.as_view()),
    path('updateemployee/<pk>', views.UpdateEmployee.as_view()),
    path('deleteemployee/<pk>', views.DeleteEmployee.as_view()),
    path('accountstatement/',views.AccountStatement, name='homeaccount'),
    path('addincome/',views.AddIncome.as_view()),
    path('addexpense/',views.AddExpense.as_view()),

]
