from django.urls import path
from . import views

urlpatterns = [
    path('tabela-parametros/', views.tabela_parametros, name='tabela_parametros'),
]