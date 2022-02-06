from django.contrib import admin

from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['format_nome', 'format_descricao']
    search_fields = ['nome', 'descricao']

    def format_nome(self, obj):
        return obj.nome.capitalize()

    def format_descricao(self, obj):
        return obj.descricao.capitalize()

    format_nome.short_description = 'Nome'
    format_descricao.short_description = 'Descrição'



admin.site.register(Categoria, CategoriaAdmin)
