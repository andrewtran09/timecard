from django import forms
from .models import ContractRatesHeader, ContractRatesDetails, RateUnit


class AddNewHeaderForm(forms.ModelForm):
    class Meta:
        model = ContractRatesHeader
        fields = "__all__"
        exclude = ["ContractID"]


class AddNewDetailsForm(forms.ModelForm):
    #series = forms.ModelChoiceField(queryset=ContractRatesDetails.object.all())
    class Meta:
        model = ContractRatesDetails
        fields = "__all__"
        exclude = ["ContractDetailID", "last_updated_by", "ContractID", "RateUnitID", "Rates", "LastModifiedOn"]

class AddNewRateUnitForm(forms.ModelForm):
    class Meta:
        model = RateUnit
        fields = "__all__"
        exclude = ["RateUnitID"]



