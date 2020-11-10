from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    quantidade = models.IntegerField()
    validade = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('validade',)

    def __str__(self):
        return self.nome
