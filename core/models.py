from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

