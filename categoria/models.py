from django.db import models

class Categoria(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome.capitalize()
