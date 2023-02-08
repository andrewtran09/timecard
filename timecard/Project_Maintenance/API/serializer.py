from rest_framework import serializers
from Project_Maintenance.models import ProjectMaintenance
from datetime import date


class ProjectSerializer(serializers.Serializer):
    project_id = serializers.IntegerField()
    project_number = serializers.IntegerField()
    project_name = serializers.CharField(max_length=1024)
    project_location = serializers.CharField(max_length=2056)
    project_duration = serializers.IntegerField()
    project_manager = serializers.CharField(max_length= 1024)
    last_modified_on = serializers.DateField(write_only=True,default=date.today())

    def create(self, validated_data):
        return ProjectMaintenance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.project_number = validated_data.get('project_number', instance.project_number)
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.project_location = validated_data.get('project_location', instance.project_location)
        instance.project_duration = validated_data.get('project_duration', instance.project_duration)
        instance.project_manager = validated_data.get('project_manager', instance.project_manager)
        instance.last_modified_on = validated_data.get('last_modified_on', instance.last_modified_on)
        instance.save()
        return instance