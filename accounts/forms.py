from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)
    primeiro_nome = forms.CharField(required=True)
    sobrenome = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "primeiro_nome", "sobrenome")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email