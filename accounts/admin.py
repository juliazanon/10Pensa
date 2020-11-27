from django.contrib import admin
from .models import Produto, Receita, Ingrediente

class IngredienteInline(admin.TabularInline):
    model = Ingrediente

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'validade')
    list_filter = ('nome', 'validade')
    date_hierarchy = 'validade'
    search_fields = ('nome',)
    raw_id_fields = ('usuario',)

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    inlines = [IngredienteInline,]
    list_display = ('nome', 'descricao')
    list_filter = ('nome',)
    search_fields = ('nome',)
    raw_id_fields = ('usuario',)

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade')
    list_filter = ('nome',)
    search_fields = ('nome',)
    raw_id_fields = ('receita',)
