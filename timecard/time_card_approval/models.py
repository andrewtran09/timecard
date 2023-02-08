from django.db import models


# Create your models here.
class TimeCardSubmission(models.Model):
    time_card_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey("Project_Maintenance.ProjectMaintenance", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    work_desc = models.CharField(max_length=100)
    last_modified_on = models.DateTimeField(auto_now=True)
    #last_updated_by = models.ForeignKey("User_maintenance.UserMaintenance", on_delete=models.CASCADE)

    manager = models.Manager()


class TimeCardDetails(models.Model):
    designation_choices = [("Manager", "Manager"),
                           ("Labor", "Labor")]
    vehicle_choices = [("Trailer", "Trailer"),
                       ("Pickup Truck", "Pickup Truck")]
    hotel_code_choices = [("Actual Cost", "Actual Cost"),
                          ("Flat Rate", "Flat Rate")]
    break_time_choices = [(5, "5 minutes"),
                      (10, "10 minutes"),
                      (15, "15 minutes"),
                      (20, "20 minutes"),
                      (25, "25 minutes"),
                      (30, "30 minutes"),
                      (35, "35 minutes"),
                      (40, "40 minutes"),
                      (45, "45 minutes"),
                      (60, "1 hour"),
                      (120, "2 hour"),
                      (180, "3 hour"),
                      (240, "4 hour"),
                      (300, "5 hour"),
                      (360, "6 hour"),
                      (420, "7 hour"),
                      (480, "8 hour")]

    time_card_detail_id = models.AutoField(primary_key=True)
    time_card_id = models.ForeignKey(TimeCardSubmission, on_delete=models.CASCADE)
    designation = models.CharField(max_length=10, choices=designation_choices, default="Labor")
    person_who_worked = models.CharField(max_length=100)
    code_id = models.ForeignKey("labor_code_maintenance.LaborCodeMaintenance", on_delete=models.CASCADE)
    small_tools = models.BooleanField(default=False)
    per_diem = models.BooleanField(default=False)
    ppe = models.BooleanField(default=False)
    prp = models.BooleanField(default=False)
    pfp = models.BooleanField(default=False)
    vehicle = models.CharField(max_length=20, choices=vehicle_choices, default="Trailer")
    mileage = models.IntegerField()
    hotel_code = models.CharField(max_length=20, choices=hotel_code_choices)
    hotel_cost = models.DecimalField(max_digits=6, decimal_places=2)
    start_time = models.TimeField()
    end_time = models.TimeField()
    break_time = models.IntegerField(choices=break_time_choices, default=5)
    total_hour = models.IntegerField(editable=False)
    last_modified_on = models.DateTimeField(auto_now=True)
    #last_updated_by = models.ForeignKey("User_maintenance.UserMaintenance", on_delete=models.CASCADE)

    manager = models.Manager()


class TimeCardStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    time_card_id = models.ForeignKey(TimeCardSubmission, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    rejection_reason = models.CharField(max_length=100)
    last_modified_on = models.DateTimeField(auto_now=True)
    #last_updated_by = models.ForeignKey("User_maintenance.UserMaintenance", on_delete=models.CASCADE)

    manager = models.Manager()
