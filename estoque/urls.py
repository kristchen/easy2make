from django.urls import path, include
from .views import ProdutoCreate, ProdutoUpdate, CategoriaCreate, CategoriaUpdate

urlpatterns = [
    path('produto/adicionar/', ProdutoCreate.as_view(), name='produto-adicionar'),
    path('produto/<int:pk>/', ProdutoUpdate.as_view(), name='produto-alterar'),
    path('categoria/adicionar/', CategoriaCreate.as_view(), name='categoria-adicionar'),
    path('categoria/<int:pk>/', CategoriaUpdate.as_view(), name='categoria-alterar')
]