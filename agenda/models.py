from django.db import models
import json

# Create your models here.
class Evento:
    id = 1
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link
        self.id = Evento.id
        Evento.id += 1

obj_evento1 = Evento("JavaScript", "BackEnd", None, "https://www.google.com.br")
obj_evento2 = Evento("Python", "FullStack", "Rio de Janeiro","https://www.google.com.br")
obj_evento3 = Evento("Csharp", "BackEnd", "Cuiabá","https://www.google.com.br")
lista_eventos = [obj_evento1, obj_evento2, obj_evento3]