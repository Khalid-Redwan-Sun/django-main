from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
<<<<<<< HEAD

    def payment_completed_view(request):
        return render(request, 'core/payment_completed.html')

    def payment_failed_view(request):
        return render(request, 'core/payment_failed.html')
=======
>>>>>>> 4c91c8f0505e05f4b243f31cc1871d4815965e58
