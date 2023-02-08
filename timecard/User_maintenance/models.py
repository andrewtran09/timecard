from django.db import models

# Create your models here.
class UserRole(models.Model):
    RoleID = models.AutoField(primary_key = True)
    RoleName = models.CharField(max_length=100,blank=False)
    RoleDescription = models.CharField(max_length= 3000,blank=True)

    objects = models.Manager()

class UserMaintenance(models.Model):
    user_id = models.AutoField(primary_key = True)
    FirstName = models.CharField(max_length= 1024,blank = False)
    LastName = models.CharField(max_length= 1024,blank=False)
    PrimaryNumber = models.CharField(max_length= 10,blank=False)
    EmailAddress = models.EmailField(blank=False)
    UserPassword = models.CharField(max_length=1024, blank=False)
    UserRoleID = models.ForeignKey("User_maintenance.UserRole", on_delete=models.CASCADE)
    Company = models.CharField(max_length=1024,blank=False)
    Active =  models.BooleanField(default=1)
    last_modified_on = models.DateField(auto_now=True, blank=False)

    objects = models.Manager()