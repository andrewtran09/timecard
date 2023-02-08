from django.db import models


# Create your models here.
class SuppliesCodeMaintenance(models.Model):
    supplies_code_id = models.AutoField(primary_key=True)
    sc_desc = models.CharField(max_length=100, blank=False)
    sc_billing_code = models.CharField(max_length=20, blank=False)
    sc_default_rates = models.IntegerField()
    sc_active = models.BooleanField(default=1)

    manager = models.Manager()
