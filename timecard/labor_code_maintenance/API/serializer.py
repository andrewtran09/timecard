from rest_framework import serializers
from labor_code_maintenance.models import LaborCodeMaintenance


class LaborSerializer(serializers.Serializer):
    labor_code_id = serializers.IntegerField()
    lc_desc = serializers.CharField(max_length=100)
    lc_billing_code = serializers.CharField(max_length=20)
    lc_default_rates = serializers.IntegerField()
    lc_active = serializers.BooleanField(default=1)

    def create(self, validated_data):
        return LaborCodeMaintenance.manager.create(**validated_data)

    def update(self, instance, validated_data):
        instance.labor_code_id = validated_data.get('labor_code_id', instance.labor_code_id)
        instance.lc_desc = validated_data.get('lc_desc', instance.lc_desc)
        instance.lc_billing_code = validated_data.get('lc_billing_code', instance.lc_billing_code)
        instance.lc_default_rates = validated_data.get('lc_default_rates', instance.lc_default_rates)
        instance.lc_active = validated_data.get('lc_active', instance.lc_active)
        instance.save()
        return instance