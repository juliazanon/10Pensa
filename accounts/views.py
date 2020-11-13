from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Produto

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserCreationFormWithEmail

class ProdutoListView(ListView):
    model = Produto
    template_name = 'accounts/perfil.html'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'accounts/produto_new.html'
    fields = '__all__'

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'accounts/produto_edit.html'
    fields = '__all__'

class SignUpView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/perfil_edit.html'

@login_required
def perfil(request):
    user = request.user
    args = {'user': user}
    return render(request, 'accounts/perfil.html', args)

""" def perfil(request, username):
    user = User.objects.get(username=username)
    context = {
       "user": user
    }

    return render(request, 'perfil.html', context) """