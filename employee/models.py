from django.db import models  

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 
    username = models.CharField(max_length=50, unique=True)  # Username field
    password = models.CharField(max_length=100)  # Password field
    status   = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('inactive', 'Inactive')],
        default='active'
    )  # Status field with choices 

    
    class Meta:  
        db_table = "employee"  
