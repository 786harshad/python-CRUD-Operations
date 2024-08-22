from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ename', 'eemail', 'econtact', 'username')  
    # Optional: Customizing the form layout
    fields = ('ename', 'eemail', 'econtact', 'username', 'password', 'status')  

admin.site.register(Employee, EmployeeAdmin)