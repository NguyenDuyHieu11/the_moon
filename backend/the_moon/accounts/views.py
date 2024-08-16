from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm # UserCreationForm is specifically designed to work with Django's user model. After submitting the form, data in the form will be validated against the expected field of the user model.
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"