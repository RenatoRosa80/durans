from django.urls import path
from . import views

urlpatterns = [
    path('', views.fazer_reserva, name='fazer_reserva'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('atualizar/<int:id>/', views.atualizar_reserva, name='atualizar_reserva'),
    path('deletar/<int:id>/', views.deletar_reserva, name='deletar_reserva'),
    path('status/<int:id>/<str:novo_status>/', views.alterar_status, name='alterar_status'),
]
