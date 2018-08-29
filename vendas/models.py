from django.db import models
from estoque.models import Produto
from clientes.models import Cliente
from .choices import VENDA_SITUACAO_CHOICES
import datetime

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='compras')
    data = models.DateField(blank=False, default=datetime.date.today)
    situacao = models.CharField(max_length=1, blank=False, default='P', choices=VENDA_SITUACAO_CHOICES)

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    quantidade = models.PositiveIntegerField(blank=False, default=1)

