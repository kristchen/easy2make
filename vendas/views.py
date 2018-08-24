from django.shortcuts import render
from django.views.generic import TemplateView
from json_views.views import JSONFormView
from .forms import VendasForm, ItemVendaForm
from .models import Venda

class VendasCreateForm(TemplateView):
    template_name = 'vendas_form.html'

class VendasCreateAPI(JSONFormView):
   
    form_class = VendasForm
    def post(self, request, *args, **kwargs):
        return __post__(self, VendasCreateAPI, request, args, kwargs)

class ItemVendaCreateAPI(JSONFormView):
   
    form_class = ItemVendaForm
    def post(self, request, *args, **kwargs):
        return __post__(self, ItemVendaCreateAPI, request, args, kwargs)


def __post__(self, classView, request, args, kwargs):
    
    form = self.form_class(request.POST)
    print(request.POST)
    if form.is_valid():
        return self.render_to_response(self.get_context_data(id=form.save().id, sucess=True))
    return super(classView, self).post(self, request, args, kwargs)


 