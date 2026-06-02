from django.db import models


class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    tempo_preparacao = models.PositiveIntegerField()
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.titulo
