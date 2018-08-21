from django.db import models
from estoque.models import Produto
from clientes.models import Cliente
import datetime

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    data = models.DateField(blank=False, default=datetime.date.today)

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    quantidade = models.PositiveIntegerField(blank=False, default=0)

