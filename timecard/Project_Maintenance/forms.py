from django import forms
from .models import ProjectMaintenance

class AddNewForm(forms.ModelForm):
    class Meta:
        model = ProjectMaintenance
        fields = "__all__"
        exclude = ["project_id"]