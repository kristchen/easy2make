from django.forms import ModelForm
from .models import Venda

class VendaForm(ModelForm):
    model = Venda
    fields = ['']