from django.shortcuts import render, redirect
from .forms import ClienteForm, ReservaForm
from .models import Reserva, Cliente
from django.contrib import messages
from django.shortcuts import get_object_or_404

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if not nome or not email:
            messages.error(request, "Nome e e-mail são obrigatórios.")
        else:
            Cliente.objects.create(nome=nome, email=email, telefone=telefone)
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('home')

    return render(request, 'cadastrar_cliente.html')

def home(request):
    reservas = Reserva.objects.all()
    return render(request, 'home.html', {'reservas': reservas})

def nova_reserva(request):
    clientes = Cliente.objects.all()  # lista todos os clientes já cadastrados

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        data = request.POST.get('data')
        hora = request.POST.get('hora')  # Novo campo de hora
        quantidade_pessoas = request.POST.get('quantidade_pessoas')

        if not cliente_id or not data or not quantidade_pessoas:
            messages.error(request, "Todos os campos são obrigatórios.")
        else:
            try:
                cliente = Cliente.objects.get(id=cliente_id)
                Reserva.objects.create(
                    cliente=cliente,
                    data=data,
                    hora=hora,  # Adiciona o campo de hora
                    quantidade_pessoas=quantidade_pessoas
                )
                messages.success(request, "Reserva cadastrada com sucesso!")
                return redirect('home')
            except Cliente.DoesNotExist:
                messages.error(request, "Cliente não encontrado.")

    return render(request, 'nova_reserva.html', {'clientes': clientes})

def apagar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    messages.success(request, "Reserva apagada com sucesso!")
    return redirect('home')

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        data = request.POST.get('data')
        hora = request.POST.get('hora')  # Novo campo de hora 
        quantidade_pessoas = request.POST.get('quantidade_pessoas')

        if not cliente_id or not data or not quantidade_pessoas:
            messages.error(request, "Todos os campos são obrigatórios.")
        else:
            cliente = Cliente.objects.get(id=cliente_id)
            reserva.cliente = cliente
            reserva.data = data
            reserva.hora = hora  # Atualiza o campo de hora
            reserva.quantidade_pessoas = quantidade_pessoas
            reserva.save()
            messages.success(request, "Reserva atualizada com sucesso!")
            return redirect('home')

    return render(request, 'editar_reserva.html', {
        'reserva': reserva,
        'clientes': clientes
    })
