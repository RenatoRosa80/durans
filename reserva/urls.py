from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nova/', views.nova_reserva, name='nova_reserva'),
    path('cliente/novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('reserva/<int:id>/editar/', views.editar_reserva, name='editar_reserva'),
    path('reserva/<int:id>/apagar/', views.apagar_reserva, name='apagar_reserva'),
]
