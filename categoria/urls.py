from xml.etree.ElementInclude import include
from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'categoria', GetAllCategorias)

urlpatterns = [
    path('', include(router.urls))
]