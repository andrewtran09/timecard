from rest_framework import serializers
from Equipment_code_maintenance.models import EquipmentCodeMaintenance

class EquipmentCodeMaintenanceSerializer(serializers.Serializer):
    equipment_id = serializers.IntegerField(read_only=True)
    equipment_code = serializers.CharField(max_length=100)
    equipment_billing_code = serializers.CharField(max_length=20)
    equipment_default_rates = serializers.IntegerField()
    equipment_active = serializers.BooleanField()

    def create(self, validated_data):
        return EquipmentCodeMaintenance.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.equipment_id = validated_data.get('equipment_id', instance.equipment_id)
        instance.equipment_code = validated_data.get('equipment_code', instance.equipment_code)
        instance.equipment_billing_code = validated_data.get('equipment_billing_code', instance.equipment_billing_code)
        instance.equipment_default_rates = validated_data.get('equipment_default_rates', instance.equipment_default_rates)
        instance.equipment_active = validated_data.get('equipment_active', instance.equipment_active)

        instance.save()

        return instance
