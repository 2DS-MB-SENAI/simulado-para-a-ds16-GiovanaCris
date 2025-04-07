from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    paginas = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo