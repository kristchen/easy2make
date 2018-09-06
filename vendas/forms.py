from django.forms import ModelForm, DateField
from .models import Venda, ItemVenda
from django.forms.widgets import DateInput

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente']

class VendaSearchForm(ModelForm):

    data_inicio = DateField(label='Data inicial', required=False, input_formats=['%Y-%m-%d'], widget=DateInput(attrs={'type': 'date'}))
    data_fim = DateField(label='Data final', required=False, input_formats=['%Y-%m-%d'], widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Venda
        fields = ['situacao']

class ItemVendaForm(ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto','venda']

class ItemVendaUpdateForm(ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['quantidade']