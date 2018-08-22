from django.urls import path, include
from .views import VendasForm

urlpatterns = [
    path('', VendasForm.as_view(), name='vendas-form')
]

