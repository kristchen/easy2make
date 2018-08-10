from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto, Categoria
from .forms import ProdutoForm

class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'adicionar_produto_form.html'       

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request)
        if form.is_valid():
            form.save()
            return super(ProdutoCreate, self).form_valid(form)
        else:
            return render(request, self.template_name, {'form': form})

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['descricao']
    template_name = 'adicionar_categoria_form.html'       