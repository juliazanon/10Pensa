from django.contrib import admin
from .models import Produto, Receita

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'validade')
    list_filter = ('nome', 'validade')
    date_hierarchy = 'validade'
    search_fields = ('nome',)
    raw_id_fields = ('usuario',)

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    list_filter = ('nome',)
    search_fields = ('nome',)
    raw_id_fields = ('usuario',)
