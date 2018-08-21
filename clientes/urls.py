from django.urls import path, include
from .views import ClienteCreate, ClienteUpdate, ClienteList, ClienteListAPI

urlpatterns = [
    path('adicionar/', ClienteCreate.as_view(), name='cliente-adicionar'),
    path('alterar/<int:pk>/', ClienteUpdate.as_view(), name='cliente-alterar'),
    path('pesquisar/', ClienteList.as_view(), name='cliente-pesquisar'),
    path('', ClienteListAPI.as_view())
]