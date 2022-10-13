from django.shortcuts import render
#from nomedaapp.forms import EstoqueForm, HospedeForm
from nomedaapp.models import Estoque, People
from django.views.generic import CreateView
from django.urls import reverse_lazy


class Hospedes(CreateView):
    template_name = "Hóspedes.html"
    model = People
    
    fields = ["nome", "nasc", "cpf", "numero_telefone", "cidade", "cep", "n_casa"]

class EstoqueCreateView (CreateView):
    template_name = "Estoque.html"
    model = Estoque
    #form_class = EstoqueForm