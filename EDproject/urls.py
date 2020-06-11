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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupPage),
    path('', views.HomePage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.AdminHomePage),
    path('instituteinfo/', views.InstituteInfo),
    path('allclasses/', views.AllClasses.as_view(),name='home'),
    path('newclass/', views.NewClass.as_view()),
    path('editclass/', views.EditClass),
    path('update/<pk>', views.UpdateClass.as_view()),
    path('delete/<pk>', views.DeleteClass.as_view()),
    path('addsubjects/', views.AddSubjects.as_view()),
    path('subjectstoclasses/', views.SubjectstoClasses.as_view()),
]
