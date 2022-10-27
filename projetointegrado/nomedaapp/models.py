from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from projetointegrado import settings
#def __str__(self):
    #return self.description
    
class People(models.Model):
    
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length =12)
    Data_De_Nascimento = models.DateField(null=True, blank=True)
    numero_telefone = models.IntegerField(null=True, blank=True)
    cep = models.CharField(max_length =9)
    cidade = models.CharField(max_length =225)
    Numero_da_Casa = models.IntegerField(null=True, blank=True)
    Contato_De_Emergência = models.IntegerField(null=True, blank=True)
    Observações = models.CharField(max_length=225)
    
    def __str__(self):
        return self.nome
    
class Estoque(models.Model):
    codigo=models.IntegerField(null=True, blank=True)
    produto = models.CharField(max_length = 50)
    quantidade= models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.nome
    
    
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
    
class galeria (models.Model):
    descricao=models.CharField(max_length=225)
    img= models.ImageField(upload_to=settings.MEDIA_ROOT)


    
