from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from .models import Produto, Categoria
from .forms import ProdutoForm, ProdutoListForm
from json_views.views import JSONListView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProdutoCreate(SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'adicionar_produto_form.html'
    success_message = 'Produto cadastrado com sucesso!'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProdutoCreate, self).dispatch( *args, **kwargs)       

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return super(ProdutoCreate, self).form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

class ProdutoUpdate(SuccessMessageMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'detalhe_produto_form.html'
    success_message = 'Produto alterado com sucesso!'
    
    def get_success_url(self):
        return reverse('estoque:produto-alterar', kwargs=self.kwargs)


class ProdutoFilter(BaseFilter):
    search_fields = {
        'descricao' : ['descricao'],          
    }

class ProdutoList(SearchListView):
    model = Produto
    template_name = 'pesquisar_produto_form.html'
    paginate_by = 8
    form_class = ProdutoListForm
    filter_class = ProdutoFilter

class ProdutoListAPI(JSONListView):
    model = Produto
    
    def post(self, request, *args, **kwargs):
        return super(ProdutoListAPI, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        descricao = self.request.POST.dict().get('descricao')
        
        return Produto.objects.filter(descricao__icontains=descricao)

class CategoriaCreate(SuccessMessageMixin, CreateView):
    model = Categoria
    fields = ['descricao']
    template_name = 'adicionar_categoria_form.html'
    success_message = 'Categoria cadastrada com sucesso!'

class CategoriaUpdate(SuccessMessageMixin, UpdateView):
    model = Categoria
    fields = ['descricao']
    template_name = 'detalhe_categoria_form.html'
    success_message = 'Categoria alterada com sucesso!'

    def get_success_url(self):
        return reverse('estoque:categoria-alterar', kwargs=self.kwargs)

class CategoriaList(ListView):
    model = Categoria
    template_name = 'pesquisar_categoria_form.html'
    paginate_by = 8