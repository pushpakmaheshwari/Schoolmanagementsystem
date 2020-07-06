from django.shortcuts import render
from EDApp.forms import SignupForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from EDApp.models import Info, Classes, Students, Employee, Account
from django.urls import reverse
from django.db.models import Sum

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
    total_students = Students.objects.all().count()
    total_employee = Employee.objects.all().count()
    income_sum = list(Account.objects.aggregate(Sum('income')).values())[0]  #sum of income amount.
    expense_sum = list(Account.objects.aggregate(Sum('expense')).values())[0]
    total_profit = income_sum - expense_sum
    return render(request, 'EDApp/dashboardpage.html', {'total_students':total_students, 'total_employee':total_employee, 'total_profit':total_profit})


class AllClasses(ListView):
    model = Classes

class NewClass(CreateView):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students','marks']
    def get_success_url(self):
        return reverse('homeclass')

def EditClass(request):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students']
    return render(request, 'EDApp/editclass.html')


class UpdateClass(UpdateView):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students','marks']
    def get_success_url(self):
        return reverse('homeclass')

class DeleteClass(DeleteView):
    model = Classes
    fields = ['name_of_class','monthly_fees','total_students']
    def get_success_url(self):
        return reverse('homeclass')

class AddSubjects(CreateView):
    model = Classes
    fields = ['subjects','marks']
    template_name = 'EDApp/addsubjects.html'
    def get_success_url(self):
        return reverse('homeclass')

class SubjectstoClasses(ListView):
    model = Classes
    template_name = 'EDApp/subjectstoclasses.html'

class AllStudents(ListView):
    model = Students

class NewStudent(CreateView):
    model = Students
    fields = '__all__'
    def get_success_url(self):
        return reverse('homestudent')

class DeleteStudent(DeleteView):
    model = Students
    fields = '__all__'
    def get_success_url(self):
        return reverse('homestudent')

class UpdateStudent(UpdateView):
    model = Students
    fields = '__all__'
    def get_success_url(self):
        return reverse('homestudent')

class Instituteinfo(ListView):
    model = Info

class Updateinfo(UpdateView):
    model = Info
    fields = '__all__'
    def get_success_url(self):
        return reverse('homeinstitute')


class AdmissionLetter(ListView):
    model = Students
    template_name = 'EDApp/admissionletter.html'
    context_object_name = 'reg_no'

class PrintDetail(DetailView):
    model = Students
    fields = '__all__'
    template_name = 'EDApp/printfile.html'
    def get_success_url(self):
        return reverse('homestudent')

class AllEmployees(ListView):
    model = Employee


class NewEmployees(CreateView):
    model = Employee
    fields = '__all__'
    def get_success_url(self):
        return reverse('homeemployee')

class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    def get_success_url(self):
        return reverse('homeemployee')

class DeleteEmployee(DeleteView):
    model = Employee
    fields = '__all__'
    def get_success_url(self):
        return reverse('homeemployee')


def AccountStatement(request):
    account = Account.objects.all()
    income_sum = list(Account.objects.aggregate(Sum('income')).values())[0]  #sum of income amount.
    expense_sum = list(Account.objects.aggregate(Sum('expense')).values())[0]
    total_sum = income_sum - expense_sum
    return render(request, 'EDApp/account_list.html', {'account':account, 'income_sum':income_sum, 'expense_sum':expense_sum, 'total_sum':total_sum})

class AddIncome(CreateView):
    model = Account
    fields = ['date','description','income']
    template_name = 'EDApp/income_form.html'
    def get_success_url(self):
        return reverse('homeaccount')

class AddExpense(CreateView):
    model = Account
    fields = ['date','description','expense']
    template_name = 'EDApp/expense_form.html'
    def get_success_url(self):
        return reverse('homeaccount')
