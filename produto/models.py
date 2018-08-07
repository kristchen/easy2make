from django.db import models


class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    marca = models.CharField(max_length=255, null=True)
    modelo = models.CharField(max_length=255, null=True)
    imagem = models.ImageField(null=True)

