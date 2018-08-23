from django.db import models
from django.shortcuts import reverse
from django.core.validators import RegexValidator


class Cliente(models.Model):

    nome = models.CharField(max_length=255, blank=False)
    telefone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    telefone = models.CharField(validators=[telefone_regex], max_length=17, blank=True)
    endereco = models.CharField(max_length=255, blank=False)

    def get_absolute_url(self):
        return reverse('clientes:cliente-pesquisar')