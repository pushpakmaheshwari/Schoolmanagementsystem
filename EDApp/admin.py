from django.contrib import admin
from EDApp.models import Classes
from EDApp.models import Students
# Register your models here.

admin.site.register(Classes)
admin.site.register(Students)

admin.site.site_header = 'EdSystango Admin'
