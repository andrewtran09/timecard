from rest_framework import serializers
from ..models import *
from datetime import date

class UserRoleserializer(serializers.Serializer):
    RoleID = serializers.IntegerField(read_only=True)
    RoleName = serializers.CharField(max_length=100)
    RoleDescription = serializers.CharField(max_length=3000)

    def create(self, validated_data):
        return UserRole.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.RoleID = validated_data.get('RoleID',instance.RoleID)
        instance.RoleName = validated_data.get('RoleName',instance.RoleName)
        instance.RoleDescription = validated_data.get('RoleDescription',instance.RoleDescription)
        instance.save()
        return instance







class  UserMaintenanceserilaizer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    FirstName = serializers.CharField(max_length=1024)
    LastName = serializers.CharField(max_length=1024)
    PrimaryNumber = serializers.CharField(max_length=10)
    EmailAddress = serializers.EmailField(read_only=True)
    UserPassword = serializers.CharField(max_length=1024)
    UserRoleID = serializers.IntegerField(read_only=True)
    Company = serializers.CharField(max_length=1024)
    Active = serializers.BooleanField(default=1)
    last_modified_on = serializers.DateTimeField(default=date.today())


    def create(self, validated_data):
        return UserMaintenance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id',instance.user_id)
        instance.FirstName = validated_data.get('FirstName',instance.FirstName)
        instance.LastName = validated_data.get('LastName',instance.LastName)
        instance.PrimaryNumber = validated_data.get('PrimaryNumber',instance.PrimaryNumber)
        instance.EmailAddress = validated_data.get('EmailAddress',instance.EmailAddress)
        instance.UserPassword = validated_data.get('UserPassword',instance.UserPassword)
        instance.UserRoleID = validated_data.get('UserRoleID',instance.UserRoleID)
        instance.Company = validated_data.get('Company',instance.Company)
        instance.Active = validated_data.get('Active',instance.Active)
        instance.last_modified_on = validated_data.get('last_modified_on',instance.last_modified_on)
        instance.save()
        return instance