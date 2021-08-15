from django.urls.base import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
