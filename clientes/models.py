from django.db import models
from django.shortcuts import reverse

class Cliente(models.Model):

    nome = models.CharField(max_length=255, blank=False)
    endereco = models.CharField(max_length=255, blank=False)

    def get_absolute_url(self):
        return reverse('clientes:cliente-pesquisar')