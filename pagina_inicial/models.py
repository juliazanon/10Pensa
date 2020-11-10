from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    quantidade = models.IntegerField()
    validade = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        ordering = ('validade',)

    def get_absolute_url(self):
        return reverse('produto_edit', args=[self.pk])

    def __str__(self):
        return self.nome
