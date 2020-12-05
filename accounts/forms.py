from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
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
        fields = ['nome','descricao',]

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

    def __init__(self, *args, **kwargs):
        super(AdicionarReceitasForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('nome'),
                Field('owner'),
                Fieldset('Adicionar ingredientes',
                    Formset('ingrediente')),
                Field('descricao'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

class AdicionarIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente 
        fields = ['nome', 'quantidade', 'tipo',]

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
            'tipo': forms.TextInput(attrs={
                                        'class': 'form-control', 
                                        'id': 'grupo', 
                                        'name': 'grupo',
                                        'placeholder': 'xícara, colher, mg...'}),
        }

IngredienteFormSet = inlineformset_factory(
    Receita, Ingrediente, form = AdicionarIngredientesForm, extra = 1, can_delete = True)

