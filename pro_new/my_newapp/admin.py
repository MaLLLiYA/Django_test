from django.contrib import admin

# Register your models here.
from my_newapp.models import Student, Bookinfo,Peopleinfo

admin.site.register(Student)
admin.site.register(Bookinfo)
admin.site.register(Peopleinfo)
