from django.urls import path, include
from .views import ProdutoCreate, CategoriaCreate

urlpatterns = [
    path('produto/adicionar/', ProdutoCreate.as_view(), name='produto-adicionar'),
    path('categoria/adicionar/', CategoriaCreate.as_view(), name='categoria-adicionar')
]