from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/home.html'), name='home'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact')
]