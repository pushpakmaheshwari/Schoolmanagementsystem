from django.contrib import admin
from EDApp.models import Classes,Students,Info, Employee, Account

# Register your models here.

admin.site.register(Classes)
admin.site.register(Students)
admin.site.register(Info)
admin.site.register(Employee)
admin.site.register(Account)

admin.site.site_header = 'EdSystango Admin'
