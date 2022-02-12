from django.contrib import admin

from .models import Cartao

class CartaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    
    def captalize_nome(self, obj):
        return obj.nome.capitalize()
    
    captalize_nome.short_description = 'Nome'

admin.site.register(Cartao, CartaoAdmin)
