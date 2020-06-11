from django.shortcuts import render
from EDApp.forms import SignupForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from EDApp.models import Classes
from EDApp.models import Students
from django.urls import reverse
# Create your views here.



def SignupPage(request):
    signupform = SignupForm()
    mydict = {'signupform':signupform}
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user=signupform.save()
            user.set_password(user.password)
            user.save()
            mydict.update({'msg':'Registered Successfully'})
    return render(request, 'EDApp/signup.html',context=mydict)



def HomePage(request):
    return render(request, 'EDApp/homepage.html')

def AdminHomePage(request):
    return render(request, 'EDApp/dashboardpage.html')

def InstituteInfo(request):
    return render(request, 'EDApp/instituteinfo.html')


class AllClasses(ListView):
    model = Classes

class NewClass(CreateView):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students']
    def get_success_url(self):
        return reverse('home')

def EditClass(request):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students']
    return render(request, 'EDApp/editclass.html')


class UpdateClass(UpdateView):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students']
    def get_success_url(self):
        return reverse('home')

class DeleteClass(DeleteView):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students']
    def get_success_url(self):
        return reverse('home')

class AddSubjects(CreateView):
    model = Classes
    fields = ['subjects','marks']
    template_name = 'EDApp/addsubjects.html'
    def get_success_url(self):
        return reverse('home')

class SubjectstoClasses(ListView):
    model = Classes
    template_name = 'EDApp/subjectstoclasses.html'
