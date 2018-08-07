from django.urls import path, include
from .views import ProdutoCreate

urlpatterns = [
    path('adicionar/', ProdutoCreate.as_view(), name='adicionar')
]