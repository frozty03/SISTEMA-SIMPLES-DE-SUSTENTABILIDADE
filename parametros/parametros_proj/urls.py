from django.contrib import admin
from django.urls import path
from ponderacao import urls, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tabela-parametros/', views.tabela_parametros, name='tabela_parametros'),
]

