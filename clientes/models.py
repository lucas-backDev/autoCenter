from django.db import models

# Create your models here.
class Cliente(models.Model):
  nome = models.CharField(max_length=128)
  sobrenome = models.CharField(max_length=128)
  email = models.EmailField(max_length=128)
  cpf = models.CharField(max_length=11)

  def __str__(self) -> str:
    return self.nome
  
class Carro(models.Model):
  carro = models.CharField(max_length=128)
  placa = models.CharField(max_length=7)
  ano = models.IntegerField()
  cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
  lavagens = models.IntegerField(default=0)
  consertos = models.IntegerField(default=0)

  def __str__(self) -> str:
    return self.carro
  
