from django.db import models

from .trabalho import Trabalho

class Avaliacao(models.Model):
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    descricao = models.CharField(max_length=100)
    trabalho = models.ForeignKey(Trabalho, related_name="trabalhos", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, nome: {self.trabalho} | nota: {self.nota}"
