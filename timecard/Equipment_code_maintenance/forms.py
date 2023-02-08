from django import forms
from .models import EquipmentCodeMaintenance


class AddNewForm(forms.ModelForm):
    class Meta:
        model = EquipmentCodeMaintenance
        fields = "__all__"
        exclude = ["equipment_id"]

