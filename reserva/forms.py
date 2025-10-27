from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome', 'email', 'telefone', 'data', 'hora', 'quantidade_pessoas']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'HH:MM'}),
            'quantidade_pessoas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'placeholder': 'Número de Pessoas'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome Completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu Email'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Telefone'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'Endereço de Email',
            'telefone': 'Número de Telefone',
            'data': 'Data da Reserva',
            'hora': 'Hora da Reserva',
            'quantidade_pessoas': 'Número de Pessoas',
        }
