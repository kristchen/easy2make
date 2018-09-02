from django.urls import path, include
from .views import VendaCreateForm, VendaCupomDetail, VendaUpdateAPI, ItemVendaUpdateAPI, ItemVendaDeleteAPI, VendaCreateAPI, ItemVendaCreateAPI, VendaDeleteAPI

urlpatterns = [
    path('', VendaCreateForm.as_view(), name='vendas-create-form'),
    path('<int:pk>/cupom/', VendaCupomDetail.as_view()),
    path('adicionar/', VendaCreateAPI.as_view()),
    path('remover/<int:pk>/', VendaDeleteAPI.as_view()),
    path('alterar/<int:pk>/', VendaUpdateAPI.as_view()),
    path('itens/adicionar/', ItemVendaCreateAPI.as_view()),
    path('itens/remover/<int:pk>/', ItemVendaDeleteAPI.as_view()),
    path('itens/alterar/<int:pk>/', ItemVendaUpdateAPI.as_view())
]

