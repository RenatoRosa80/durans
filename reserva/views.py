from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reserva
from .forms import ReservaForm

def fazer_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva enviada com sucesso! Aguarde confirmação.')
            return redirect('fazer_reserva')
    else:
        form = ReservaForm()
    return render(request, 'fazer_reserva.html', {'form': form})

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.all().order_by('-criado_em')
    return render(request, 'lista_reservas.html', {'reservas': reservas})

@login_required
def atualizar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva atualizada!')
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'atualizar_reserva.html', {'form': form})

@login_required
def alterar_status(request, id, novo_status):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.status = novo_status
    reserva.save()
    messages.success(request, f'Status alterado para {novo_status}')
    return redirect('lista_reservas')

@login_required
def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    messages.success(request, 'Reserva removida.')
    return redirect('lista_reservas')
