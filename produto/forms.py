from django.forms import ModelForm, ModelChoiceField
from .models import Produto, Categoria

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        categoria = ModelChoiceField(queryset=Categoria.objects.all(),to_field_name="categoria",empty_label="Nao existem categorias")  
        fields = ['descricao','categoria','preco', 'marca', 'modelo','imagem']
    