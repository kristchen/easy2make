from django.urls import path, include
from .views import ClienteCreate

urlpatterns = [
    path('adicionar/', ClienteCreate.as_view(), name='cliente-adicionar'),
]