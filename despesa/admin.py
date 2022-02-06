from django.contrib import admin

from .models import Despesa


class DespesaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Despesa, DespesaAdmin)
