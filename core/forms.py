
from django.core.mail.message import EmailMessage
from django import forms
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())


    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n Assunto {mensagem}'

        mail = EmailMessage(
            subject='Email enviado com sucesso', 
            body=conteudo,            
            from_email='contato@seudominio.com.br',
            to=['contato@seumail.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']

        