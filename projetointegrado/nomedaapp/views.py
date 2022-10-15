from django.shortcuts import render
#from nomedaapp.forms import EstoqueForm, HospedeForm
from nomedaapp.models import Estoque, People
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView



class HospedesView (CreateView):
    template_name = "Hóspedes.html"
    model = People
    fields = ["nome", "Data_De_Nascimento", "cpf", "numero_telefone", "cidade", "cep", "Numero_da_Casa", 'Contato_De_Emergência', 'Observações']
    success_url= '/menu/'
    

class HospedesListView (ListView):
    template_name = "VerHospedes.html"
    model = People

class HospedeDeleteView(DeleteView):
    model = People
    success_url = '/ver_hospedes/'
    
class EstoqueView (CreateView):
    template_name = "Estoque.html"
    model = Estoque
    fields = ['codigo', 'produto', 'quantidade']
    success_url= '/menu/'   
    
    
class EstoqueListView (ListView):
    template_name = "VerEstoque.html"
    model = Estoque
    
