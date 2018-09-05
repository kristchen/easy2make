from django.forms import ModelForm
from .models import Venda, ItemVenda

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']

class VendaUpdateForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['situacao','data']

class ItemVendaForm(ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto','venda']

class ItemVendaUpdateForm(ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['quantidade']