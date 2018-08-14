from django.urls import path, include
from .views import ProdutoCreate, ProdutoUpdate, ProdutoList, CategoriaCreate, CategoriaUpdate, CategoriaList

urlpatterns = [
    path('produto/adicionar/', ProdutoCreate.as_view(), name='produto-adicionar'),
    path('produto/<int:pk>/', ProdutoUpdate.as_view(), name='produto-alterar'),
    path('produto/pesquisar/', ProdutoList.as_view(), name='produto-pesquisar'),
    path('categoria/adicionar/', CategoriaCreate.as_view(), name='categoria-adicionar'),
    path('categoria/<int:pk>/', CategoriaUpdate.as_view(), name='categoria-alterar'),
    path('categoria/pesquisar/', CategoriaList.as_view(), name='categoria-pesquisar')
]