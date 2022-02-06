from rest_framework import viewsets

from .models import Categoria
from.serializers import CategoriaSerializer


class CategoriasView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('-created_at')
    serializer_class = CategoriaSerializer