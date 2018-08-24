from django.urls import path, include
from .views import VendasCreateForm, VendasCreateAPI, ItemVendaCreateAPI

urlpatterns = [
    path('', VendasCreateForm.as_view(), name='vendas-create-form'),
    path('adicionar/', VendasCreateAPI.as_view()),
    path('itens/adicionar/', ItemVendaCreateAPI.as_view())
]

