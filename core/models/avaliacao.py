# from django.db import models

# from .trabalho import Trabalho, User


# class Avaliacao(models.Model):
#     nota = models.DecimalField(max_digits=3, decimal_places=1)
#     descricao = models.CharField(max_length=100)
#     trabalho = models.ForeignKey(Trabalho, related_name="trabalhos", on_delete=models.PROTECT, null=True, blank=True)
#     nome = models.ForeignKey(User, related_name="usuarios", on_delete=models.PROTECT, null=True, blank=True)

#     def __str__(self):
#         return f"id:{self.id}, nome: {self.nome} | nota: {self.nota}"

#     def media(self):
#         if self.nota.count() == 0:
#             return 0
#         return sum(Avaliacao.nota for avaliacao in self.nota.all()) / self.notas.count()
