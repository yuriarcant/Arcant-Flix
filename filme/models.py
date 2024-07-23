from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISE", 'Análise'),
    ("PROGRAMACAO", 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros')
)


# criar filme

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    vizualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.titulo


# criar os episodios

class Episodio(models.Model):
    filme = models.ForeignKey(
        "Filme", related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self) -> str:
        return self.filme.titulo + "-" + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField('Filme')
