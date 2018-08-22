from django.shortcuts import render
from django.views.generic import TemplateView

class VendasForm(TemplateView):
    template_name = 'vendas_form.html'