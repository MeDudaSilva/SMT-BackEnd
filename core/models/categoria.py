from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"({self.id}) nome: {self.nome} | {self.simbolo}"
