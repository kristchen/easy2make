from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm

class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'adicionar_produto_form.html'       

    def form_invalid(self, form):
        form.save(commit=True)
        return super(ProdutoCreate, self).form_valid(form)