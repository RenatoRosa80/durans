
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute('href'));
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        const duration = 500; // tempo da animação em ms (0.5 segundos)
        let start = null;

        function step(timestamp) {
            if (!start) start = timestamp;
            const progress = timestamp - start;
            const progressRatio = Math.min(progress / duration, 1);
            window.scrollTo(0, startPosition + distance * progressRatio);
            if (progress < duration) requestAnimationFrame(step);
        }

        requestAnimationFrame(step);
    });
});

// Lógica para exibir o alerta de sucesso ou o modal de reserva
    document.addEventListener('DOMContentLoaded', function () {
    const reservaModalElement = document.getElementById('reservaModal');
    const alerta = document.getElementById('success-alert');

    // Inicializa o modal (mas não abre automaticamente)
    const reservaModal = new bootstrap.Modal(reservaModalElement, { backdrop: 'static', keyboard: false });

    // Exibe o alerta de sucesso, se houver
    if (alerta && alerta.classList.contains('alert-success')) {
        alerta.style.display = 'block';
        setTimeout(() => alerta.classList.add('show'), 10);

        setTimeout(() => {
            alerta.classList.remove('show');
            setTimeout(() => alerta.style.display = 'none', 500);
        }, 3000);
    }

    // Reabre o modal apenas se houver erros no formulário
    const formErrors = reservaModalElement.querySelectorAll('.text-danger');
    if (formErrors.length > 0) {
        reservaModal.show();
    }
});
