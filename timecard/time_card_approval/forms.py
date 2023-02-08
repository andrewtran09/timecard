from django import forms
from .models import TimeCardStatus, TimeCardSubmission, TimeCardDetails


class AddNewForm(forms.ModelForm):
    class Meta:
        model = TimeCardStatus
        fields = "__all__"
