from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .models import LaborCodeMaintenance
from .forms import AddNewForm


# Create your views here.
class ShowList(ListView):
    model = LaborCodeMaintenance
    ordering = ["labor_code_id"]
    queryset = LaborCodeMaintenance.manager.all()


class AddNew(View):
    form_class = AddNewForm
    template_name = "labor_code_maintenance/add_new_form.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_lc_list"))

        return render(request, self.template_name, {"form": form})
