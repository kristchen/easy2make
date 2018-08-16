from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Cliente
from search_views.search import SearchListView
from search_views.filters import BaseFilter


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome','endereco']
    template_name = 'adicionar_cliente_form.html'


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome','endereco']
    template_name = 'detalhe_cliente_form.html'


class ClienteFilter(BaseFilter):
    search_fields = {
        'nome' : ['nome'],          
    }

class ClienteList(SearchListView):
    model = Cliente
    template_name = 'pesquisar_cliente_form.html'
    filter_class = ClienteFilter