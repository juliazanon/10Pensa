from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from .models import Produto, Receita

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *

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

class ProdutoListView(ListView):
    model = Produto
    template_name = 'accounts/perfil.html'

    def get_queryset(self):
        return Produto.objects.filter(usuario=self.request.user)

class ProdutoCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Produto
    form_class = AdicionarProdutosForm
    template_name = 'accounts/produto_new.html'
    success_message = "%(field)s - criado com sucesso"
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )

class ProdutoUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Produto
    template_name = 'accounts/produto_edit.html'
    form_class = AdicionarProdutosForm
    success_url = reverse_lazy('perfil')
    success_message = "%(field)s - criado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )

class ProdutoDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Produto
    template_name = 'accounts/produto_delete.html'
    success_url = reverse_lazy('perfil')
    success_message = "Produto deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(ProdutoDeleteView,self).delete(request, *args, **kwargs)


class ReceitaListView(ListView):
    model = Receita
    template_name = 'accounts/receitas.html'

    def get_queryset(self):
        return Receita.objects.filter(usuario=self.request.user)

class ReceitaDetailView(DetailView):
    model = Receita
    template_name = 'accounts/receita_detail.html'


class ReceitaCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Receita
    form_class = AdicionarReceitasForm
    template_name = 'accounts/receita_new.html'
    success_message = "Receita de %(field)s criada com sucesso"
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )

class ReceitaUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Receita
    template_name = 'accounts/receita_edit.html'
    form_class = AdicionarReceitasForm
    success_url = reverse_lazy('receitas')
    success_message = "Receita de %(field)s - criada com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )

class ReceitaDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Receita
    template_name = 'accounts/receita_delete.html'
    success_url = reverse_lazy('perfil')
    success_message = "Receita Deletada com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(ReceitaDeleteView,self).delete(request, *args, **kwargs)