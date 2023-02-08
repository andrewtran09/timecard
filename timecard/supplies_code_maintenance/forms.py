from django import forms
from .models import SuppliesCodeMaintenance


class AddNewForm(forms.ModelForm):
    class Meta:
        model = SuppliesCodeMaintenance
        fields = "__all__"
        exclude = ["supplies_code_id"]
