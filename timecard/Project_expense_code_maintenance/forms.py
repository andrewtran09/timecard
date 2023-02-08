from django import forms
from .models import ProjectExpenseCodeMaintenance


class AddNewForm(forms.ModelForm):
    class Meta:
        model = ProjectExpenseCodeMaintenance
        fields = "__all__"
        exclude = ["expense_id"]

