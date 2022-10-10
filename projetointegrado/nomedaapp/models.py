from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class People(models.Model):
    hóspedes = models.CharField(max_length=50)
    cpf = models.CharField(max_length =12)
    rg = models.IntegerField("")
    nasc = models.DateField()
    numero_telefone = models.IntegerField("")
    rua = models.CharField(max_length =50000)
    cep = models.CharField(max_length =9)
    bairro = models.CharField(max_length =50000)
    cidade = models.CharField(max_length =50000)
    n_casa = models.IntegerField("")

class Estoque(models.Model):
    produto = models.CharField(max_length = 50) , models.IntegerField("")
    