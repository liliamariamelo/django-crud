from django.shortcuts import render, redirect
from core.forms import PessoaForm
from .models import Pessoa

def home(request):
    return render(request, 'portal/home.html')

def pessoa(request):
    pessoas = Pessoa.objects.all()
    context = {
        'pessoas': pessoas
    }
    return render(request, "portal/pessoa.html", context)

def pessoa_add(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa')
    else:
        form = PessoaForm()

    context = {
        'form': form
    }
    return render(request, 'portal/pessoa_add.html', context)

def pessoa_editar(request, pessoa_pk):
    pessoa = Pessoa.objects.get(pk=pessoa_pk)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)  
        if form.is_valid():
            form.save()
            return redirect('pessoa')
    else:
        form = PessoaForm(instance=pessoa) 

    context = {
        'form': form,
        'pessoa': pessoa,
    }
    return render(request, 'portal/pessoa_editar.html', context)

def pessoa_excluir(request, pessoa_pk):
    pessoa = Pessoa.objects.get(pk=pessoa_pk)
    pessoa.delete()
    return redirect('pessoa')

