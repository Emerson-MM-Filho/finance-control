from django.db import models

class Cartao(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.nome.capitalize()
