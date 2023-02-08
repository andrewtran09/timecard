from rest_framework import serializers
from django.db import models
from Project_Maintenance.models import ProjectMaintenance
from User_maintenance.models import UserMaintenance
from ..models import ContractRatesHeader,RateUnit,ContractRatesDetails,ContractRateTransmit
from datetime import date

class ContractRatesHeaderserializer(serializers.Serializer):
    ContractID = serializers.IntegerField(read_only=True)
    ProjectID_id = serializers.IntegerField(read_only=True)
    SubContractor = serializers.CharField(max_length=512)
    RatesAgreedBy = serializers.CharField(max_length=512)
    LastModifiedOn = serializers.DateTimeField(default=date.today())
    #last_updated_by = models.ForeignKey(UserMaintenance, on_delete=models.CASCADE)

    # object = models.Manager()

    def create(self, validated_data):
        return ContractRatesHeader.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.ContractID = validated_data.get('ContractID',instance.ContractID)
        instance.ProjectID_id = validated_data.get('ProjectID_id',instance.ProjectID_id)
        instance.SubContractor = validated_data.get('SubContractor',instance.SubContractor)
        instance.RatesAgreedBy = validated_data.get('RatesAgreedBy',instance.RatesAgreedBy)
        instance.LastModifiedOn = validated_data.get('LastModifiedOn',instance.LastModifiedOn)
        instance.save()
        return instance




class RateUnitserializer(serializers.Serializer):
    RateUnitID = serializers.IntegerField(read_only=True)
    UnitName = serializers.CharField(max_length=512)
    UnitValue = serializers.CharField(max_length=512)
    # object = models.Manager()

    def create(self, validated_data):
        return RateUnit.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.RateUnitID = validated_data.get('RateUnitID',instance.RateUnitID)
        instance.UnitName = validated_data.get('UnitName',instance.UnitName)
        instance.UnitValue = validated_data.get('UnitValue',instance.UnitValue)
        instance.save()
        return instance

class ContractRatesDetailsserializer(serializers.Serializer):
    # MY_CHOICES = (
    #     ('Per Hour', "per hour"),
    #     ('Per Day', "per day"),
    #     ('Entire Project', "entire project"),
    # )
    # my_field = MultiSelectField(choices=MY_CHOICES, max_length=20)
    ContractDetailID = serializers.IntegerField(read_only=True)
    ContractID = serializers.IntegerField(read_only=True)
    CodeID = serializers.CharField(max_length=512)
    Rates = serializers.CharField(max_length=512)
    RateUnitID = serializers.IntegerField(read_only=True)
    LastModifiedOn = serializers.DateTimeField(default=date.today())
    #last_updated_by = models.ForeignKey(UserMaintenance, on_delete=models.CASCADE)

    # object = models.Manager()

    def create(self, validated_data):
        return ContractRatesDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ContractDetailID = validated_data.get('ContractDetailID', instance.ContractDetailID)
        instance.ContractID = validated_data.get('ContractID', instance.ContractID)
        instance.CodeID = validated_data.get('CodeID', instance.CodeID)
        instance.Rates = validated_data.get('Rates', instance.Rates)
        instance.RateUnitID = validated_data.get('RateUnitID', instance.RateUnitID)
        instance.LastModifiedOn  = validated_data.get('LastModifiedOn', instance.LastModifiedOn)
        instance.save()
        return instance


class ContractRateTransmitserializer(serializers.Serializer):
    TransmitID = serializers.IntegerField(read_only=True)
    ContractID = serializers.IntegerField(read_only=True)
    EmailtoSent = serializers.CharField(max_length=64)
    # SentByUser = serializers.ForeignKey(UserMaintenance, related_name='sent_UserMaintenance', on_delete=models.CASCADE)
    LastModifiedOn = serializers.DateTimeField(default=date.today())
    #last_updated_by = models.ForeignKey(UserMaintenance, related_name='last_UserMaintenance', on_delete=models.CASCADE)

    # object = models.Manager()

    def create(self, validated_data):
        return ContractRateTransmit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ContractID = validated_data.get('ContractID', instance.ContractID)
        instance.TransmitID = validated_data.get('TransmitID', instance.TransmitID)
        instance.EmailtoSent = validated_data.get('EmailtoSent', instance.EmailtoSent)
        instance.LastModifiedOn = validated_data.get('LastModifiedOn', instance.LastModifiedOn)
        instance.save()
        return instance



from rest_framework import serializers
from django.db import models
from Project_Maintenance.models import ProjectMaintenance
from User_maintenance.models import UserMaintenance
from ..models import ContractRatesHeader,RateUnit,ContractRatesDetails,ContractRateTransmit
from datetime import date

class ContractRatesHeaderserializer(serializers.Serializer):
    ContractID = serializers.IntegerField(read_only=True)
    ProjectID_id = serializers.IntegerField(read_only=True)
    SubContractor = serializers.CharField(max_length=512)
    RatesAgreedBy = serializers.CharField(max_length=512)
    LastModifiedOn = serializers.DateTimeField(default=date.today())
    #last_updated_by = models.ForeignKey(UserMaintenance, on_delete=models.CASCADE)


    def create(self, validated_data):
        return ContractRatesHeader.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.ContractID = validated_data.get('ContractID',instance.ContractID)
        instance.ProjectID_id = validated_data.get('ProjectID_id',instance.ProjectID_id)
        instance.SubContractor = validated_data.get('SubContractor',instance.SubContractor)
        instance.RatesAgreedBy = validated_data.get('RatesAgreedBy',instance.RatesAgreedBy)
        instance.LastModifiedOn = validated_data.get('LastModifiedOn',instance.LastModifiedOn)
        instance.save()
        return instance




class RateUnitserializer(serializers.Serializer):
    RateUnitID = serializers.IntegerField(read_only=True)
    UnitName = serializers.CharField(max_length=512)
    UnitValue = serializers.CharField(max_length=512)
    # object = models.Manager()

    def create(self, validated_data):
        return RateUnit.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.RateUnitID = validated_data.get('RateUnitID',instance.RateUnitID)
        instance.UnitName = validated_data.get('UnitName',instance.UnitName)
        instance.UnitValue = validated_data.get('UnitValue',instance.UnitValue)
        instance.save()
        return instance

class ContractRatesDetailsserializer(serializers.Serializer):
    # MY_CHOICES = (
    #     ('Per Hour', "per hour"),
    #     ('Per Day', "per day"),
    #     ('Entire Project', "entire project"),
    # )
    # my_field = MultiSelectField(choices=MY_CHOICES, max_length=20)
    ContractDetailID = serializers.IntegerField(read_only=True)
    ContractID = serializers.IntegerField(read_only=True)
    CodeID = serializers.CharField(max_length=512)
    Rates = serializers.CharField(max_length=512)
    RateUnitID = serializers.IntegerField(read_only=True)
    LastModifiedOn = serializers.DateTimeField(default=date.today())
    #last_updated_by = models.ForeignKey(UserMaintenance, on_delete=models.CASCADE)

    # object = models.Manager()

    def create(self, validated_data):
        return ContractRatesDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ContractDetailID = validated_data.get('ContractDetailID', instance.ContractDetailID)
        instance.ContractID = validated_data.get('ContractID', instance.ContractID)
        instance.CodeID = validated_data.get('CodeID', instance.CodeID)
        instance.Rates = validated_data.get('Rates', instance.Rates)
        instance.RateUnitID = validated_data.get('RateUnitID', instance.RateUnitID)
        instance.LastModifiedOn  = validated_data.get('LastModifiedOn', instance.LastModifiedOn)
        instance.save()
        return instance


class ContractRateTransmitserializer(serializers.Serializer):
    TransmitID = serializers.IntegerField(read_only=True)
    ContractID = serializers.IntegerField(read_only=True)
    EmailtoSent = serializers.CharField(max_length=64)
    # SentByUser = serializers.ForeignKey(UserMaintenance, related_name='sent_UserMaintenance', on_delete=models.CASCADE)
    LastModifiedOn = serializers.DateTimeField(default=date.today())
    #last_updated_by = models.ForeignKey(UserMaintenance, related_name='last_UserMaintenance', on_delete=models.CASCADE)

    # object = models.Manager()

    def create(self, validated_data):
        return ContractRateTransmit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ContractID = validated_data.get('ContractID', instance.ContractID)
        instance.TransmitID = validated_data.get('TransmitID', instance.TransmitID)
        instance.EmailtoSent = validated_data.get('EmailtoSent', instance.EmailtoSent)
        instance.LastModifiedOn = validated_data.get('LastModifiedOn', instance.LastModifiedOn)
        instance.save()
        return instance



