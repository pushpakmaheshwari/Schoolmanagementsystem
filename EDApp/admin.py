from django.contrib import admin
from EDApp.models import Classes,Students,Info

# Register your models here.

admin.site.register(Classes)
admin.site.register(Students)
admin.site.register(Info)

admin.site.site_header = 'EdSystango Admin'
