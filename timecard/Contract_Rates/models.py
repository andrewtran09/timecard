from django.db import models

from Project_Maintenance.models import ProjectMaintenance
from User_maintenance.models import UserMaintenance
from multiselectfield import MultiSelectField

class ContractRatesHeader(models.Model):
    ContractID = models.AutoField(primary_key=True)
    ProjectID = models.ForeignKey(ProjectMaintenance, on_delete=models.CASCADE)
    SubContractor = models.CharField(max_length=512, blank=False)
    RatesAgreedBy = models.CharField(max_length=512, blank=False)
    LastModifiedOn = models.DateTimeField(auto_now=True)
    #last_updated_by = models.ForeignKey(UserMaintenance, on_delete=models.CASCADE)

    object = models.Manager()

class RateUnit(models.Model):
    RateUnitID = models.AutoField(primary_key=True)
    UnitName = models.CharField(max_length=512, blank=False)
    UnitValue = models.CharField(max_length=512, blank=False)

    object = models.Manager()

class ContractRatesDetails(models.Model):
    # MY_CHOICES = (
    #     ('Per Hour', "per hour"),
    #     ('Per Day', "per day"),
    #     ('Entire Project', "entire project"),
    # )
    # my_field = MultiSelectField(choices=MY_CHOICES, max_length=20)
    ContractDetailID = models.AutoField(primary_key=True)
    ContractID = models.ForeignKey(ContractRatesHeader, on_delete=models.CASCADE)
    CodeID = models.CharField(max_length=512, blank=False)
    Rates = models.CharField(max_length=512, blank=False)
    RateUnitID = models.ForeignKey(RateUnit, on_delete=models.CASCADE)
    LastModifiedOn = models.DateTimeField(auto_now=True)
    #last_updated_by = models.ForeignKey(UserMaintenance, on_delete=models.CASCADE)

    object = models.Manager()


class ContractRateTransmit(models.Model):
    TransmitID = models.AutoField(primary_key=True)
    ContractID = models.ForeignKey(ContractRatesHeader, on_delete=models.CASCADE)
    EmailtoSent = models.CharField(max_length=64, blank=False)
    SentByUser = models.ForeignKey(UserMaintenance, related_name='sent_UserMaintenance', on_delete=models.CASCADE)
    LastModifiedOn = models.DateTimeField(auto_now=True)
    #last_updated_by = models.ForeignKey(UserMaintenance, related_name='last_UserMaintenance', on_delete=models.CASCADE)

    object = models.Manager()


