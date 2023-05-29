from django.db import models
import json

# Create your models here - Django
class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)

class Evento(models.Model):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256)
    link = models.CharField(max_length=256, blank=True)
