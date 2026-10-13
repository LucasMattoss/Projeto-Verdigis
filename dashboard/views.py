from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """Página inicial da área logada. Acesso restrito a usuários autenticados."""
    return render(request, 'dashboard/dashboard.html')
