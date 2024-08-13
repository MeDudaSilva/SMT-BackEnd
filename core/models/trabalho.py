from django.db import models

from .user import User


class Trabalho(models.Model):
    dataInicio = models.DateField()
    prazo = models.DateField()
    DataTermino = models.DateField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=1)
    # usuario = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name="usuarios", blank=True, null=True)

    def __str__(self):
        return f"({self.id}) nome: {self.usuario} | Iniciou-se: {self.dataInicio} | Prazo : {self.prazo} | Terminou em: {self.DataTermino}"
