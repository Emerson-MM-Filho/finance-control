from django.contrib import admin

from .models import Despesa
from .utils import format_despesa_valor

class DespesaAdmin(admin.ModelAdmin):
    list_display = ['format_data_da_despesa', 'captalize_nome', 'format_valor', 'captalize_categoria', 'parcelas', 'cartao', 'format_tipo']
    list_filter = ['data_da_despesa', 'categoria', 'parcelas', 'cartao', 'tipo']
    search_fields = ['nome', 'valor', 'parcelas']

    def format_data_da_despesa(self, obj):
        format = '%d/%m/%Y'
        return obj.data_da_despesa.strftime(format)
    
    def format_valor(self, obj):
        return format_despesa_valor(obj)

    def format_tipo(self, obj):
        return obj.get_tipo_display()

    def captalize_nome(self, obj):
        return obj.nome.capitalize()
    
    def captalize_categoria(self, obj):
        return obj.categoria.nome.capitalize()
    
    format_data_da_despesa.short_description = 'Data da Despesa'
    format_valor.short_description = 'Valor'
    captalize_nome.short_description = 'Nome'
    captalize_categoria.short_description = 'Categoria'
    format_tipo.short_description = 'Tipo'

admin.site.register(Despesa, DespesaAdmin)
