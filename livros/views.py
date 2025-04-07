from django.shortcuts import render
from .models import Livros
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import LivroSerializer

def listar_livros(request):
    livros = Livros.objects.all()
    return render (request, 'livros.html', {'livros':livros})

@api_view(['GET', 'POST'])
def methods_livros(request):
    if request.method == 'GET':
        livros = Livros.objects.all()
        titulo = request.query_params.get('titulo')
        autor = request.query_params.get('autor')
        paginas = request.query_params.get('paginas')

        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
               