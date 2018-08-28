from django.urls import path, include
from .views import VendasCreateForm, ItemVendaDeleteAPI, VendasCreateAPI, ItemVendaCreateAPI, VendasDeleteAPI

urlpatterns = [
    path('', VendasCreateForm.as_view(), name='vendas-create-form'),
    path('adicionar/', VendasCreateAPI.as_view()),
    path('remover/<int:pk>/', VendasDeleteAPI.as_view()),
    path('itens/adicionar/', ItemVendaCreateAPI.as_view()),
    path('itens/remover/<int:pk>/', ItemVendaDeleteAPI.as_view())
]

