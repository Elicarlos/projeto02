
from django import forms
from django.shortcuts import redirect, render
from . forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from . models import Produto
from django.shortcuts import redirect

# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            # Forma de recuperar

            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']

            form.send_email()
            messages.success(request, 'Email enviado com sucesso')
            form = ContatoForm()

            
        else:
            messages.error(request, 'Erro ao enviar o email')


    context = {
        'form': form
    }
    return render (request, 'contato.html', context )

def produto(request):
    # print(f'Usuario: { request.user}')
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                # prod = form.save(commit=False)
                # print(f'Nome {prod.nome}, preco {prod.preco} estoque {prod.estoque}')
                form.save()
                messages.success(request, 'Produto Salvo com sucesso')
                form = ProdutoModelForm()

            else:
                messages.error(request, 'Erro ao salvar o produto')
        
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
        
    else:
        return redirect('index')
