from django.shortcuts import render
from EDApp.forms import SignupForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from EDApp.models import Info, Classes, Students, Employee, Account, EdsysClass, StudentAttendance, Attendance
from django.urls import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect

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



# Classes Business codes: -------------------------------------------------------------------->

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



# Students Business codes: ------------------------------------------------------------------------->

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




# Institute  Business codes: --------------------------------------------------------------->

class Instituteinfo(ListView):
    model = Info

class Updateinfo(UpdateView):
    model = Info
    fields = '__all__'
    def get_success_url(self):
        return reverse('homeinstitute')



# Admission letter  Business codes: ------------------------------------------------------------------------------>

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






# Employees  Business codes: --------------------------------------------------------------->

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





# Account Business codes: --------------------------------------------------------------->

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





# Attendance Business codes: --------------------------------------------------------------->
'''
class MarkStudentsAttendance(ListView):
    model = Classes
    template_name = 'EDApp/markstudentsattendance.html'


class MarkEmployeesAttendance(ListView):
    model = Employee
    template_name = 'EDApp/markemployeesattendance.html'


class StudentsAttendanceReport(ListView):
    model = Students
    template_name = 'EDApp/studentsattendancereport.html'


class EmployeesAttendanceReport(ListView):
    model = Employee
    template_name = 'EDApp/employeesattendancereport.html'


#class AttendenceSheet(DetailView):
#    model = Students
#    template_name = 'EDApp/attendencesheet.html'


def AttendenceSheet(request):
    if request.method == 'POST':
        cid = method.POST['class_id']
'''


def AllClassAttendance(request):
    classes = EdsysClass.objects.all()
    if request.method == 'POST' and 'search' in request.POST:
        dropdown_val = request.POST.get('dropdownlist')
        return HttpResponseRedirect("/studentattendance"+dropdown_val)
    return render(request, 'EDApp/allattendance.html', {'classes':classes})


            #View for saving student attendance
def StudentAttendance(request, pk):
    allclass = EdsysClass.objects.get(id=pk)
    if request.method == 'POST':

        name = request.POST.get('studentname')
        sid = request.POST.get('studentid')
        classes = request.POST.get('class')
        date = "2020-12-06"
        val = request.POST.get('x')

        data = Attendance.objects.create(
                                # id = sid,
                                Class = classes,
                                date = date,
                                StudentName = name,
                                status = val,
                            )
        data.save()
        # return HttpResponse("/studentattendance")

    return render(request, 'EDApp/studentattendance.html', {'allclass':allclass})

            # ListView For Student Attendance Report.
class StudentAttedanceReport(ListView):
    model = Attendance
    context_object_name = "studentreport"
    template_name = "EDApp/studentattendancereport.html"

class EmployeeAttedanceReport(ListView):
    model = Attendance
    context_object_name = "employeereport"
    template_name = "EDApp/employeeattendancereport.html"


def EmployeeAttendance(request):
    allemp = Employee.objects.all()
    return render(request, 'EDApp/employeeattendance.html', {'allemp':allemp})


# Fees Business codes: --------------------------------------------------------------->

class SubmitFees(ListView):
    model = Students
    template_name = 'EDApp/submitfees.html'


class Details(DetailView):
    model = Students
    template_name = 'EDApp/detailofstudent.html'
