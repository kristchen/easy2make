from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView
from .models import Cliente
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.contrib.messages.views import SuccessMessageMixin
from json_views.views import JSONListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ClienteCreate(SuccessMessageMixin, CreateView):
    model = Cliente
    fields = ['nome','telefone','endereco']
    template_name = 'adicionar_cliente_form.html'
    success_message = 'Cliente cadastrado com sucesso!'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return __dispatch__(self, ClienteCreate, *args, **kwargs)


class ClienteUpdate(SuccessMessageMixin, UpdateView):
    model = Cliente
    fields = ['nome','telefone','endereco']
    template_name = 'detalhe_cliente_form.html'
    success_message = 'Cliente alterado com sucesso!'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return __dispatch__(self, ClienteUpdate, *args, **kwargs)


class ClienteFilter(BaseFilter):
    search_fields = {
        'nome' : ['nome'],          
    }

class ClienteList(SearchListView):
    model = Cliente
    paginate_by = 8
    template_name = 'pesquisar_cliente_form.html'
    filter_class = ClienteFilter

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return __dispatch__(self, ClienteList, *args, **kwargs)

class ClienteListAPI(JSONListView):
    model = Cliente
    
    def post(self, request, *args, **kwargs):
        return super(ClienteListAPI, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        nome = self.request.POST.dict().get('nome')
        return Cliente.objects.filter(nome__icontains=nome)

def __dispatch__(self, classView, *args, **kwargs):
    return super(classView, self).dispatch( *args, **kwargs) 
        
