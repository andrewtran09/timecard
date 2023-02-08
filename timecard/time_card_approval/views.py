from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .models import TimeCardStatus, TimeCardSubmission, TimeCardDetails
from .forms import AddNewForm


# Create your views here.
class ShowList(ListView):
    model = TimeCardStatus
    # ordering = ["labor_code_id"]
    queryset = TimeCardStatus.manager.all()


class AddNew(View):
    form_class = AddNewForm
    template_name = "time_card_approval/add_new_form.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_time_cards_list"))

        return render(request, self.template_name, {"form": form})
