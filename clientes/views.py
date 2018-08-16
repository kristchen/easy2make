from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cliente


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome','endereco']
    template_name = 'adicionar_cliente_form.html'