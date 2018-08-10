from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    descricao = models.CharField(max_length=255, null=False)

class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    marca = models.CharField(max_length=255, blank=True, default='')
    quantidade = models.IntegerField(null=False, default=0)
    modelo = models.CharField(max_length=255, blank=True, default='')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('produto:adicionar')



