from django.shortcuts import render
from .models import Livros

def listar_livros(request):
    livros = Livros.objects.all()
    return render (request, 'livros.html', {'livros':livros})