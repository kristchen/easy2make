from django.forms import ModelForm
from .models import Venda, ItemVenda

class VendasForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']

class ItemVendaForm(ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto','venda','quantidade']