from django.db import models

# Create your models here.
class ProjectMaintenance(models.Model):
    project_id = models.AutoField(primary_key =True)
    project_number = models.IntegerField(blank = False)
    project_name = models.CharField(max_length=1024,blank=False)
    project_location = models.CharField(max_length=2056,blank=False)
    project_duration = models.IntegerField(blank = False)
    project_manager = models.CharField(max_length= 1024,blank=False)
    last_modified_on = models.DateField(blank= False)
    #last_updated_by = models.CharField(max_length=1024,blank=False)

    objects = models.Manager()