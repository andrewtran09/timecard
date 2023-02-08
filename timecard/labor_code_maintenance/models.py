from django.db import models


# Create your models here.
class LaborCodeMaintenance(models.Model):
    labor_code_id = models.AutoField(primary_key=True)
    lc_desc = models.CharField(max_length=100, blank=False)
    lc_billing_code = models.CharField(max_length=20, blank=False)
    lc_default_rates = models.IntegerField()
    lc_active = models.BooleanField(default=1)
    # last_updated_by = models.ForeignKey("user_maintenance.UserMaintenance", on_delete=models.CASCADE)

    manager = models.Manager()
