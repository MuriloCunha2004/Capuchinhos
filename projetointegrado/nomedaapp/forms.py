from django import forms
from models import NameForm
from nomedaapp.models import Estoque, People
from django.forms import ModelForm


    
class HospedeForm(ModelForm):
    class Meta:
        model = People 
        fields = ["codigo", "nome", "nasc", "cpf", "numero_telefone", "cidade", "cep", "n_casa"]
        
        
class EstoqueForm(ModelForm):
    class meta:
        model = Estoque
        fields = ['produto' , 'quantidade']
        exclude = ['codigo']
        


class ContactForm(forms.Form):
    subject =forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
    
    
        