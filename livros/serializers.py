from rest_framework import serializers
from .models import Livros

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'