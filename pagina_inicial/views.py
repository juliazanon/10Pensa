from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from .models import Produto

class PaginaListView(ListView):
    model = Produto
    template_name = 'pagina_inicial/home.html'

class PaginaCreateView(CreateView):
    model = Produto
    template_name = 'pagina_inicial/produto_new.html'
    fields = '__all__'

class PaginaUpdateView(UpdateView):
    model = Produto
    template_name = 'pagina_inicial/produto_edit.html'
    fields = '__all__'

