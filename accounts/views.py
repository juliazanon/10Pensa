from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from .models import Produto, Receita, Ingrediente

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.db import transaction

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from .forms import *

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class UserEditView(UpdateView):
    form_class = UserChangeForm
    success_url = reverse_lazy('perfil')
    template_name = 'accounts/perfil_edit.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return super().form_valid(form)

class UserDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = User
    template_name = 'accounts/excluir_usuario.html'
    success_url = reverse_lazy('perfil')
    success_message = "Usuário deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(UserDeleteView,self).delete(request, *args, **kwargs)

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        query = User.objects.filter(username=username)
        if query.exists():
            user = query[0]
            newpassword = User.objects.make_random_password(10)
            user.set_password(newpassword)
            user.save()
            message_name = 'Recuperação de Senha 10Pensa'
            message = 'A sua nova senha é: ' + \
                newpassword + 'Não se esqueça de mudá-la!'
            message_email = '10pensapoliusp@gmail.com'
            recipient = user.email

            send_mail(
                message_name,
                message,
                message_email,
                [recipient],
            )
        return redirect('login')

    else:
        return render(request, 'accounts/forgot-password.html', {})


@login_required
def perfil(request):
    user = request.user
    args = {'user': user}

    return render(request, 'accounts/perfil.html', args)

class ProdutoListView(ListView):
    model = Produto
    template_name = 'accounts/despensa.html'

    def get_queryset(self):
        return Produto.objects.filter(usuario=self.request.user)

class ProdutoCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Produto
    form_class = AdicionarProdutosForm
    template_name = 'accounts/produto_new.html'
    success_message = "%(field)s - criado com sucesso"
    success_url = reverse_lazy('despensa')

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
    success_url = reverse_lazy('despensa')
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
    success_url = reverse_lazy('despensa')
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
    success_url = reverse_lazy('receitas')

    def get_context_data(self, **kwargs):
        context = super(ReceitaCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ingrediente'] = IngredienteFormSet(
                self.request.POST, instance=self.object)
        else:
            context['ingrediente'] = IngredienteFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingrediente = context['ingrediente']
        with transaction.atomic():
            form.instance.usuario = self.request.user
            self.object = form.save()
            if ingrediente.is_valid():
                ingrediente.instance = self.object
                ingrediente.save()
        return super(ReceitaCreateView, self).form_valid(form)

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

    def get_context_data(self, **kwargs):
        context = super(ReceitaUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ingrediente'] = IngredienteFormSet(
                self.request.POST, instance=self.object)
        else:
            context['ingrediente'] = IngredienteFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingrediente = context['ingrediente']
        with transaction.atomic():
            form.instance.usuario = self.request.user
            self.object = form.save()
            if ingrediente.is_valid():
                ingrediente.instance = self.object
                ingrediente.save()
        return super(ReceitaUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )

class ReceitaDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Receita
    template_name = 'accounts/receita_delete.html'
    success_url = reverse_lazy('receitas')
    success_message = "Receita Deletada com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(ReceitaDeleteView,self).delete(request, *args, **kwargs)
