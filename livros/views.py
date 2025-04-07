from django.shortcuts import render
from .models import Livro
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import LivroSerializer

def listar_livros(request):
    livros = Livro.objects.all()
    return render (request, 'livros.html', {'livros':livros})

@api_view(['GET', 'POST'])
def methods_livros(request):
    if request.method == 'GET':
    # Colocar o patch no api view
    #     usuario = request.user
    #     serializer = UsuarioSerializer(usuario)
    #     return Response(serializer.data)
    
    # if request.method in ['PUT', 'PATCH']:
    #     parcial = request.method == patch

        try:
            livros = Livro.objects.all()
            serializer = LivroSerializer(livros, many=True)
            
        except Livro.DoesNotExist:
            return Response({'erro': 'Evento não agendado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
               