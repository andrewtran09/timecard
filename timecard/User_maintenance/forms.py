from django import forms
from .models import UserMaintenance

class AddNewForm(forms.ModelForm):
    class Meta:
        model = UserMaintenance
        fields = "__all__"
        exclude = ["user_id"]