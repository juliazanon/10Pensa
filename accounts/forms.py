from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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