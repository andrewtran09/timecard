import datetime

from rest_framework import serializers
from time_card_approval.models import TimeCardSubmission, TimeCardDetails, TimeCardStatus


class TimeCardSerializer(serializers.Serializer):
    time_card_id = serializers.IntegerField()
    project_id_id = serializers.IntegerField()
    date = serializers.DateField()
    work_desc = serializers.CharField(max_length=100)
    last_modified_on = serializers.DateField(write_only=True, default=datetime.date.today())

    # last_updated_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return TimeCardSubmission.manager.create(**validated_data)

    def update(self, instance, validated_data):
        instance.time_card_id = validated_data.get('time_card_id', instance.time_card_id)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.date = validated_data.get('date', instance.date)
        instance.work_desc = validated_data.get('work_desc', instance.work_desc)
        instance.last_modified_on = validated_data.get('last_modified_on', instance.last_modified_on)
        instance.save()
        return instance


class TimeCardDetailSerializer(serializers.Serializer):
    time_card_detail_id = serializers.IntegerField()
    time_card_id = serializers.IntegerField()
    designation = serializers.CharField(max_length=10)
    person_who_worked = serializers.CharField(max_length=100)
    code_id = serializers.IntegerField()
    small_tools = serializers.BooleanField(default=False)
    per_diem = serializers.BooleanField(default=False)
    ppe = serializers.BooleanField(default=False)
    prp = serializers.BooleanField(default=False)
    pfp = serializers.BooleanField(default=False)
    vehicle = serializers.CharField(max_length=20, default="Trailer")
    mileage = serializers.IntegerField()
    hotel_code = serializers.CharField(max_length=20)
    hotel_cost = serializers.DecimalField(max_digits=6, decimal_places=2)
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    break_time = serializers.IntegerField(default=5)
    total_hour = serializers.IntegerField()
    last_modified_on = serializers.DateTimeField(write_only=True, default=datetime.date.today())

    def create(self, validated_data):
        return TimeCardDetails.manager.create(**validated_data)

    def update(self, instance, validated_data):
        instance.time_card_detail_id = validated_data.get('time_card_detail_id', instance.time_card_detail_id)
        instance.time_card_id = validated_data.get('time_card_id', instance.time_card_id)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.person_who_worked = validated_data.get('person_who_worked', instance.person_who_worked)
        instance.code_id = validated_data.get('code_id', instance.code_id)
        instance.small_tools = validated_data.get('small_tools', instance.small_tools)
        instance.per_diem = validated_data.get('per_diem', instance.per_diem)
        instance.ppe = validated_data.get('ppe', instance.ppe)
        instance.prp = validated_data.get('prp', instance.prp)
        instance.pfp = validated_data.get('pfp', instance.pfp)
        instance.vehicle = validated_data.get('vehicle', instance.vehicle)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.hotel_code = validated_data.get('hotel_code', instance.hotel_code)
        instance.hotel_cost = validated_data.get('hotel_cost', instance.hotel_cost)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.break_time = validated_data.get('break_time', instance.break_time)
        instance.total_hour = validated_data.get('total_hour', instance.total_hour)
        instance.last_modified_on = validated_data.get('last_modified_on', instance.last_modified_on)
        instance.save()
        return instance


class TimeCardStatusSerializer(serializers.Serializer):
    status_id = serializers.IntegerField()
    time_card_id = serializers.IntegerField()
    status = serializers.CharField(max_length=20)
    rejection_reason = serializers.CharField(max_length=100)
    last_modified_on = serializers.DateField(write_only=True, default=datetime.date.today())

    # last_updated_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return TimeCardStatus.manager.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status_id = validated_data.get('status_id', instance.status_id)
        instance.time_card_id = validated_data.get('time_card_id', instance.time_card_id)
        instance.status = validated_data.get('status', instance.status)
        instance.rejection_reason = validated_data.get('rejection_reason', instance.rejection_reason)
        instance.last_modified_on = validated_data.get('last_modified_on', instance.last_modified_on)
        instance.save()
        return instance
