from django.db import models

# Create your models here.
class EquipmentCodeMaintenance(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    equipment_code = models.CharField(max_length=100, blank=False)
    equipment_billing_code = models.CharField(max_length=20, blank=False)
    equipment_default_rates = models.IntegerField()
    equipment_active = models.BooleanField(default=1)
    # last_updated_by = models.ForeignKey("user_maintenance.UserMaintenance", on_delete=models.CASCADE)

    object = models.Manager()
    
