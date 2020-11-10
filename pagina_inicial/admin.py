from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'validade')
    list_filter = ('nome', 'validade')
    date_hierarchy = 'validade'
    search_fields = ('nome',)
    raw_id_fields = ('usuario',)
