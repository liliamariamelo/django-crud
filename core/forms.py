from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        #Usar todos os atributos 
        exclude = ()

        widgets = {
        'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
        'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
        'cpf' : forms.TextInput(attrs={'class': 'form-control'}),
        'email' : forms.EmailInput(attrs={'class': 'form-control'}),
        'telefone' : forms.TextInput(attrs={'class': 'form-control'}),
    }