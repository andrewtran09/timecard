

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import ContractRatesHeader
from .forms import AddNewHeaderForm, AddNewDetailsForm, AddNewRateUnitForm


def AddNewForm(request, id=None):
    form1 = AddNewHeaderForm(request.POST or None)
    form2 = AddNewDetailsForm(request.POST or None)
    form3 = AddNewRateUnitForm(request.POST or None)
    context = {
        "form1": form1,
        "form2": form2,
        "form3": form3
    }
    if all([form1.is_valid(), form2.is_valid(), form3.is_valid()]):
        f1 = form1.save(commit=True)
        f3 = form3.save(commit=True)
        f2 = form2.save(commit=False)
        f2.ContractID = f1
        f2.RateUnitID = f3
        f2.save()

        print("form1", form1.cleaned_data)
        print("form2", form2.cleaned_data)
        print("form3", form3.cleaned_data)
        context['message'] = 'Data saved'
    return render(request, "Contract_Rates/add_new_form.html", context)

def Add_New_Contract_Rate_Page(request):
    return render(request, "Contract_Rates/add_new_page.html")
