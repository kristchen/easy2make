from django.shortcuts import render
from django.views.generic import TemplateView, View
from json_views.views import JSONFormView
from .forms import VendasForm, ItemVendaForm, ItemVendaUpdateForm
from .models import Venda, ItemVenda
from django.views.generic.detail import SingleObjectMixin

class VendasCreateForm(TemplateView):
    template_name = 'vendas_form.html'

class VendasCreateAPI(JSONFormView):
   
    form_class = VendasForm
    def post(self, request, *args, **kwargs):
        return __post__(self, VendasCreateAPI, request, args, kwargs)

class VendasDeleteAPI(JSONFormView):

    form_class = VendasForm    
    def post(self, request, *args, **kwargs):
        venda = Venda.objects.get(pk=kwargs['pk'])
        venda.delete()
        return self.render_to_response(self.get_context_data(sucess=True))

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

 