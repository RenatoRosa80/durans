from django.urls import path
from . import views

urlpatterns = [
    # Páginas do painel (só staff)
    path('reservas/', views.lista_reservas, name='lista_reserva'),
    path('reserva/editar/<int:id>/', views.atualizar_reserva, name='editar_reserva'),   
    path('reserva/deletar/<int:id>/', views.deletar_reserva, name='deletar_reserva'),
    path('reserva/status/<int:id>/<str:novo_status>/', views.alterar_status, name='alterar_status'),
    
    # Páginas abertas
    path('fazer_reserva/', views.fazer_reserva, name='fazer_reserva'),  
    path('minhas_reservas/', views.minhas_reservas, name='minhas_reservas'),  # <-- NOVA ROTA

    # Login / Logout
    path('logout/', views.logout_view, name='logout'),  
]

