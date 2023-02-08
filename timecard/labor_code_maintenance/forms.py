from django import forms
from .models import LaborCodeMaintenance


class AddNewForm(forms.ModelForm):
    class Meta:
        model = LaborCodeMaintenance
        fields = "__all__"
        exclude = ["labor_code_id"]
