from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SnacksList(TemplateView):
    template_name='snack_list.html'
