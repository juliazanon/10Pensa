from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import date
from unidecode import unidecode
import datetime as DT

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    validade = models.DateField()

    CHOICES = (
        ('Unidade', 'Unidade'),
        ('Pacote', 'Pacote'),
        ('Lata', 'Lata'),
        ('Caixa', 'Caixa'),
        ('Kg', 'Kg')
    )

    tipo = models.CharField(max_length=10, choices = CHOICES, default='Unidade')

    usuario = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        ordering = ('validade',)

    def get_absolute_url(self):
        return reverse('produto_edit', args=[self.pk])

    @property
    def is_expired(self):
        return self.validade < date.today()
    def is_close_expire(self):
        past_expire = self.validade < date.today()
        close_expire = self.validade < date.today() + DT.timedelta(days=7)
        return  not (past_expire) and close_expire

    def __str__(self):
        return self.nome

class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    descricao = models.TextField(verbose_name="Modo de Preparo")
    is_active = models.BooleanField(default=True)

    usuario = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()

    def is_valid(self):
        produtos = Produto.objects.all()
        ings_receita = Ingrediente.objects.filter(receita=self)
        valid = True
        for ing in ings_receita:
            ing_ok = False
            exist = False
            for prod in produtos:
                if unidecode(ing.nome.lower()) == unidecode(prod.nome.lower()):
                    exist = True
                if exist == True and not(prod.is_expired):
                    ing_ok = True
            if ing_ok == False:
                valid = False
        
        return valid

    def get_absolute_url(self):
        return reverse('receita_detail', args=[self.pk])

    def get_absolute_url_update(self):
        return reverse('receita_edit',args=[self.pk])

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    quantidade = models.FloatField()
    is_active = models.BooleanField(default=True)

    receita = models.ForeignKey(
        Receita, null=True, blank=True, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


