from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from .models import Produto, Categoria
from .forms import ProdutoForm, ProdutoListForm
from django.core.paginator import Paginator


class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'adicionar_produto_form.html'       

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return super(ProdutoCreate, self).form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

class ProdutoUpdate(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'detalhe_produto_form.html'
    
    def get_success_url(self):
        return reverse('estoque:produto-alterar', kwargs=self.kwargs)


class ProdutoFilter(BaseFilter):
    search_fields = {
        'descricao' : ['descricao'],          
    }

class ProdutoList(SearchListView):
    model = Produto
    template_name = 'pesquisar_produto_form.html'
    form_class = ProdutoListForm
    filter_class = ProdutoFilter

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['descricao']
    template_name = 'adicionar_categoria_form.html'

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['descricao']
    template_name = 'detalhe_categoria_form.html'

    def get_success_url(self):
        return reverse('estoque:categoria-alterar', kwargs=self.kwargs)

class CategoriaList(ListView):
    model = Categoria
    template_name = 'pesquisar_categoria_form.html'  