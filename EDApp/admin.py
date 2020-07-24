from django.contrib import admin
from EDApp.models import Classes, Students, Info, Employee, Account, EdsysClass, StudentAttendance, Attendance

# Register your models here.

admin.site.register(Classes)
admin.site.register(Students)
admin.site.register(Info)
admin.site.register(Employee)
admin.site.register(Account)
admin.site.register(EdsysClass)
admin.site.register(StudentAttendance)
admin.site.register(Attendance)

admin.site.site_header = 'EdSystango Admin'
