from django.db import models


class Genero(models.Model):
    descricao = models.CharField(max_length=1)

    def __str__(self):
        return f"({self.id}) {self.descricao}"
