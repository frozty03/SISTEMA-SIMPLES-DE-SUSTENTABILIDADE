"""
URL configuration for sustentabilidade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from sustentabilidade_app import views  # Certifique-se de importar views corretamente

urlpatterns = [
    path('', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuario/<int:id>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('relatorio/', views.relatorio, name='relatorio'),  # Nova URL adicionada
]




