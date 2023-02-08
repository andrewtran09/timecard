from rest_framework import serializers
from supplies_code_maintenance.models import SuppliesCodeMaintenance

class SuppliesCodeMaintenanceSerializer(serializers.Serializer):
    supplies_code_id = serializers.IntegerField(read_only=True)
    sc_desc = serializers.CharField(max_length=100)
    sc_billing_code = serializers.CharField(max_length=20)
    sc_default_rates = serializers.IntegerField()
    sc_active = serializers.BooleanField()

    def create(self, validated_data):
        return SuppliesCodeMaintenance.manager.create(**validated_data)

    def update(self, instance, validated_data):
        instance.supplies_code_id = validated_data.get('sc_id', instance.supplies_code_id)
        instance.sc_desc = validated_data.get('sc_code', instance.sc_desc)
        instance.sc_billing_code = validated_data.get('sc_billing_code', instance.sc_billing_code)
        instance.sc_default_rates = validated_data.get('sc_default_rates', instance.sc_default_rates)
        instance.sc_active = validated_data.get('sc_active', instance.sc_active)

        instance.save()

        return instance
