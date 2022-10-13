from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms

# Create your models here.

    
class People(models.Model):
    codigo=models.IntegerField(" ")
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length =12)
    rg = models.IntegerField("")
    nasc = models.DateField("")
    numero_telefone = models.IntegerField("")
    cep = models.CharField(max_length =9)
    cidade = models.CharField(max_length =225)
    n_casa = models.IntegerField("")


class Estoque(models.Model):
    codigo=models.IntegerField("")
    produto = models.CharField(max_length = 50)
    quantidade= models.IntegerField("")
    
    
    
    
    
class funcionários(models.Model):
    codigo=models.IntegerField("")
    nome= models.CharField(max_length=225)
    cpf = models.CharField(max_length =12)
    rg = models.IntegerField("")
    nasc = models.DateField("")
    numero_telefone = models.IntegerField("")
    rua = models.CharField(max_length =225)
    cep = models.CharField(max_length =9)
    bairro = models.CharField(max_length =225)
    cidade = models.CharField(max_length =225)
    n_casa = models.IntegerField("")
    
