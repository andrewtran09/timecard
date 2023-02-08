from rest_framework import serializers
from Project_expense_code_maintenance.models import ProjectExpenseCodeMaintenance

class ProjectExpenseCodeMaintenanceSerializer(serializers.Serializer):
    expense_id = serializers.IntegerField(read_only=True)
    expense_code = serializers.CharField(max_length=100)
    expense_billing_code = serializers.CharField(max_length=20)
    expense_default_rates = serializers.IntegerField()
    expense_active = serializers.BooleanField()

    def create(self, validated_data):
        return ProjectExpenseCodeMaintenance.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.expense_id = validated_data.get('expense_id', instance.expense_id)
        instance.expense_code = validated_data.get('expense_code', instance.expense_code)
        instance.expense_billing_code = validated_data.get('expense_billing_code', instance.expense_billing_code)
        instance.expense_default_rates = validated_data.get('expense_default_rates', instance.expense_default_rates)
        instance.expense_active = validated_data.get('expense_active', instance.expense_active)

        instance.save()

        return instance