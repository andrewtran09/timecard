from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .forms import AddNewForm
from .models import UserMaintenance

# Create your views here.
class AddNewUser(View):
    form_class = AddNewForm
    template_name = "user_maintenance/add_new_form.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_user_list"))

        return render(request, self.template_name, {"form": form})


class ShowProjectList(ListView):
    model = UserMaintenance
    ordering = ["user_id"]
    queryset = UserMaintenance.objects.all()

