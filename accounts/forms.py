from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from datetime import date

class UserCreationFormWithEmail(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user', 'type': 'password', 'id': 'senha', 'name': 'senha', 'placeholder': 'Senha'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user', 'type': 'password', 'id': 'repetirsenha', 'name': 'repetirsenha', 'placeholder': 'Repita sua senha'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                                        'id': 'username',
                                        'name': 'username',
                                        'placeholder': 'Nome de usuário'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user',
                                                 'id': 'nome',
                                                 'name': 'nome',
                                                 'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user',
                                                 'id': 'nome',
                                                 'name': 'nome',
                                                 'placeholder': 'Sobrenome'}),
                'email': forms.EmailInput(attrs={'class': 'form-control form-control-user',
                                                 'id': 'email',
                                                 'name': 'email',
                                                 'placeholder': 'Endereço de e-mail'}),
        }
    def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Este e-mail já está cadastrado.")
            return email

class AdicionarProdutosForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'tipo', 'validade']

        widgets = {
            'nome': forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'nome',
                                        'name': 'nome',
                                        'placeholder': 'Nome do produto'}),
            'quantidade': forms.NumberInput(attrs={
                                        'class': 'form-control',
                                        'id': 'quantidade',
                                        'name': 'quantidade',
                                        'step': 1}),
            'tipo': forms.Select(attrs={
                                        'class': 'form-control', 
                                        'id': 'grupo', 
                                        'name': 'grupo'}),
            'validade': forms.DateInput(attrs={
                                        'class': 'form-control',
                                        'type': 'date',
                                        'id': 'data',
                                        'name': 'data',}),
        }

class AdicionarReceitasForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'descricao',]

        widgets = {
            'nome': forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'id': 'nome',
                                        'name': 'nome',
                                        'placeholder': 'Nome da receita'}),
            'descricao': forms.Textarea(attrs={
                                        'class': 'form-control',
                                        'id': 'texto',
                                        'name': 'texto',
                                        'rows': '15',
                                        'placeholder': 'Modo de preparo'}),
        }