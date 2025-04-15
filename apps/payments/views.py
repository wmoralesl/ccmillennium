from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PaymentsListView(TemplateView):
    template_name = 'payments/list.html'