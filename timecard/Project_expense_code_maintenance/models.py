from django.db import models

# Create your models here.
class ProjectExpenseCodeMaintenance(models.Model):
    expense_id = models.AutoField(primary_key=True)
    expense_code = models.CharField(max_length=100, blank=False)
    expense_billing_code = models.CharField(max_length=20, blank=False)
    expense_default_rates = models.IntegerField()
    expense_active = models.BooleanField(default=1)
    # last_updated_by = models.ForeignKey("user_maintenance.UserMaintenance", on_delete=models.CASCADE)

    object = models.Manager()
    
