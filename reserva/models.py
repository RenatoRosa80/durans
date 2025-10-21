from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField()
    hora = models.TimeField(null=True, blank=True)  # Novo campo de hora
    quantidade_pessoas = models.IntegerField()

    def __str__(self):
        return f"{self.cliente.nome} - {self.data.strftime('%d/%m/%Y %H:%M')}"
