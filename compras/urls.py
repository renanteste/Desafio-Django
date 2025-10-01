# compras/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_compra, name='cadastrar_compra'),
]