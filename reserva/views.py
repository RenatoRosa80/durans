from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from .models import Reserva
from .forms import ReservaForm

# ------------------------
# Páginas abertas a qualquer usuário
# ------------------------
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

def minhas_reservas(request):
    reservas = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        reservas = Reserva.objects.filter(nome__iexact=nome, email__iexact=email)
        if not reservas.exists():
            messages.warning(request, "Nenhuma reserva encontrada com essas informações.")
    return render(request, 'minhas_reservas.html', {'reservas': reservas})

# ------------------------
# Login/Logout
# ------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:  # só permite staff
                login(request, user)
                return redirect('lista_reservas')
            else:
                messages.error(request, "Você não tem permissão para acessar o painel.")
        else:
            messages.error(request, "Usuário ou senha incorretos")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# ------------------------
# Páginas do painel (só staff)
# ------------------------
@staff_member_required
def lista_reservas(request):        
    reservas = Reserva.objects.filter(data__gte=timezone.now().date()).order_by('data', 'hora') # data__gte garante que só aparecem datas futuras ou de hoje
    return render(request, 'lista_reserva.html', {'reservas': reservas})    

@staff_member_required
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
    return render(request, 'editar_reserva.html', {'form': form})

@staff_member_required
def alterar_status(request, id, novo_status):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.status = novo_status
    reserva.save()
    messages.success(request, f"Status da reserva de {reserva.nome} alterado para {novo_status}.")
    return redirect('lista_reservas')

@staff_member_required
def deletar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    messages.success(request, 'Reserva removida.')
    return redirect('lista_reservas')
