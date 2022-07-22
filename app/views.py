from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import ContactUsForm


class ContactUsView(CreateView):
    form_class = ContactUsForm
    success_url = reverse_lazy('home')
    template_name = 'app/contact_us.html'
