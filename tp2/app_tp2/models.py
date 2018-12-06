from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Estoque(models.Model):
    nome = models.CharField(max_length=15)
    descricao= models.CharField(max_length=75)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
     return self.nome   