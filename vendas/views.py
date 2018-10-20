from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View, DetailView
from json_views.views import JSONFormView
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from .forms import VendaForm, ItemVendaForm, ItemVendaUpdateForm, VendaSearchForm
from .models import Venda, ItemVenda
import datetime
import json
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class VendaFilter(BaseFilter):
    search_fields = {
        'situacao' : ['situacao'],
        'data_inicio' :{ 'operator' : '__gte', 'fields':['data']},
        'data_fim' :{ 'operator' : '__lte', 'fields':['data']}          
    }


class VendaList(SearchListView):
    model = Venda
    template_name = 'pesquisar_venda_form.html'
    paginate_by = 8
    form_class = VendaSearchForm
    filter_class = VendaFilter

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return __dispatch__(self, VendaList, *args, **kwargs)

class VendaCreateForm(TemplateView):
    template_name = 'vendas_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return __dispatch__(self, VendaCreateForm, *args, **kwargs)

class VendaDetail(DetailView):
    model = Venda
    template_name = 'vendas_detalhe.html'
    
    def get_object(self):
        return __get_object__(self, VendaDetail)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return __dispatch__(self, VendaDetail, *args, **kwargs)

class VendaCupomDetail(DetailView):
    model = Venda
    template_name = 'cupom_template.html'

    def get_object(self):
        return __get_object__(self, VendaCupomDetail)
    
    def get_context_data(self, **kwargs):
        context = super(VendaCupomDetail, self).get_context_data(**kwargs)
        venda = super(VendaCupomDetail, self).get_object()
        
        items = []
        for item in venda.itens.all():
            item.total = 0
            item.total = item.quantidade * item.produto.preco
            items.append(item)
        
        context['items'] = items
        return context

class VendaCreateAPI(JSONFormView):
   
    form_class = VendaForm
    def post(self, request, *args, **kwargs):
        return __post__(self, VendaCreateAPI, request, args, kwargs)

class VendaDeleteAPI(JSONFormView):

    form_class = VendaForm    
    def post(self, request, *args, **kwargs):
        venda = Venda.objects.get(pk=kwargs['pk'])
        venda.delete()
        return self.render_to_response(self.get_context_data(sucess=True))

class VendaUpdateAPI(View):
 
    def post(self, request, *args, **kwargs):
        venda = Venda.objects.get(pk=kwargs['pk'])
        venda.situacao = 'F'
        venda.data = datetime.datetime.now()

        for item in venda.itens.all():
            produto = item.produto
            produto.quantidade -= item.quantidade
            total = item.quantidade * item.produto.preco
            produto.save()
        
        venda.total = total
        venda.save()
        
        return HttpResponse(json.dumps({'sucess':True}))

class ItemVendaCreateAPI(JSONFormView):
   
    form_class = ItemVendaForm
    def post(self, request, *args, **kwargs):
        return __post__(self, ItemVendaCreateAPI, request, args, kwargs)

class ItemVendaDeleteAPI(JSONFormView):

    form_class = ItemVendaForm
    def post(self, request, *args, **kwargs):
        item = ItemVenda.objects.get(pk=kwargs['pk'])
        item.delete()
        return self.render_to_response(self.get_context_data(sucess=True))

class ItemVendaUpdateAPI(JSONFormView):

    form_class = ItemVendaUpdateForm
    def post(self, request, *args, **kwargs):
        item = ItemVenda.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST, instance=item)
        form.save()
        return self.render_to_response(self.get_context_data(sucess=True))

def __post__(self, classView, request, args, kwargs):
    
    form = self.form_class(request.POST)
    if form.is_valid():
        return self.render_to_response(self.get_context_data(id=form.save().id, sucess=True))
    return super(classView, self).post(self, request, args, kwargs)

def __get_object__(self, classView):
    
    venda = super(classView, self).get_object()
    # caso a venda não esteja finalizada
    if venda.situacao == 'P':
        venda.total = 0
        for item in venda.itens.all():
            venda.total += (item.quantidade * item.produto.preco)
    
    return venda

def __dispatch__(self, classView, *args, **kwargs):
    return super(classView, self).dispatch( *args, **kwargs)