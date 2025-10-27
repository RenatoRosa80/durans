from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    STATUS_CHOICES = [
        ('Em espera', 'Em espera'),
        ('Confirmada', 'Confirmada'),
        ('Cancelada', 'Cancelada'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data = models.DateField()
    hora = models.TimeField()
    quantidade_pessoas = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Em espera')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.data} ({self.status})"
