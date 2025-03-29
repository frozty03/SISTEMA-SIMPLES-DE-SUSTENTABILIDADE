from django.urls import path
from .views import mostrar_parametros

urlpatterns = [
    path('', mostrar_parametros, name='mostrar_parametros'),
]